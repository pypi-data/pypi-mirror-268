# Copyright (c) 2020 PaddlePaddle Authors. All Rights Reserved. 
#   
# Licensed under the Apache License, Version 2.0 (the "License");   
# you may not use this file except in compliance with the License.  
# You may obtain a copy of the License at   
#   
#     http://www.apache.org/licenses/LICENSE-2.0    
#   
# Unless required by applicable law or agreed to in writing, software   
# distributed under the License is distributed on an "AS IS" BASIS, 
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  
# See the License for the specific language governing permissions and   
# limitations under the License.

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import sys
import datetime
from typing import Dict
from pyparsing import Optional
import six
import copy
import json

import paddle
import paddle.distributed as dist

from ppdet.utils.checkpoint import save_model
from ppdet.metrics import get_infer_results
from typing import Dict
# from ppdet.utils.object_detection_metric_api import TrainMetric, Metric, LOSS_METRIC, MAP_METRIC, AP50_METRIC, AR_METRIC
from gaea_operator.metric.types.object_detection_metric import TrainMetric, BaseTrainMetric
import fcntl
from ppdet.utils.logger import setup_logger
logger = setup_logger('ppdet.engine')

__all__ = [
    'Callback', 'ComposeCallback', 'LogPrinter', 'Checkpointer',
    'VisualDLWriter', 'SniperProposalsGenerator'
]


class Callback(object):
    def __init__(self, model):
        self.model = model

    def on_step_begin(self, status):
        pass

    def on_step_end(self, status):
        pass

    def on_epoch_begin(self, status):
        pass

    def on_epoch_end(self, status):
        pass

    def on_train_begin(self, status):
        pass

    def on_train_end(self, status):
        pass


class ComposeCallback(object):
    def __init__(self, callbacks):
        callbacks = [c for c in list(callbacks) if c is not None]
        for c in callbacks:
            assert isinstance(
                c, Callback), "callback should be subclass of Callback"
        self._callbacks = callbacks

    def on_step_begin(self, status):
        for c in self._callbacks:
            c.on_step_begin(status)

    def on_step_end(self, status):
        for c in self._callbacks:
            c.on_step_end(status)

    def on_epoch_begin(self, status):
        for c in self._callbacks:
            c.on_epoch_begin(status)

    def on_epoch_end(self, status):
        for c in self._callbacks:
            c.on_epoch_end(status)

    def on_train_begin(self, status):
        for c in self._callbacks:
            c.on_train_begin(status)

    def on_train_end(self, status):
        for c in self._callbacks:
            c.on_train_end(status)


class LogPrinter(Callback):
    def __init__(self, model):
        super(LogPrinter, self).__init__(model)

    def on_step_end(self, status):
        if dist.get_world_size() < 2 or dist.get_rank() == 0:
            mode = status['mode']
            if mode == 'train':
                epoch_id = status['epoch_id']
                step_id = status['step_id']
                steps_per_epoch = status['steps_per_epoch']
                training_staus = status['training_staus']
                batch_time = status['batch_time']
                data_time = status['data_time']

                epoches = self.model.cfg.epoch
                batch_size = self.model.cfg['{}Reader'.format(mode.capitalize(
                ))]['batch_size']

                logs = training_staus.log()
                space_fmt = ':' + str(len(str(steps_per_epoch))) + 'd'
                if step_id % self.model.cfg.log_iter == 0:
                    eta_steps = (epoches - epoch_id) * steps_per_epoch - step_id
                    eta_sec = eta_steps * batch_time.global_avg
                    eta_str = str(datetime.timedelta(seconds=int(eta_sec)))
                    ips = float(batch_size) / batch_time.avg
                    fmt = ' '.join([
                        'Epoch: [{}]',
                        '[{' + space_fmt + '}/{}]',
                        'learning_rate: {lr:.6f}',
                        '{meters}',
                        'eta: {eta}',
                        'batch_cost: {btime}',
                        'data_cost: {dtime}',
                        'ips: {ips:.4f} images/s',
                    ])
                    fmt = fmt.format(
                        epoch_id,
                        step_id,
                        steps_per_epoch,
                        lr=status['learning_rate'],
                        meters=logs,
                        eta=eta_str,
                        btime=str(batch_time),
                        dtime=str(data_time),
                        ips=ips)
                    logger.info(fmt)
            if mode == 'eval':
                step_id = status['step_id']
                if step_id % 100 == 0:
                    logger.info("Eval iter: {}".format(step_id))

    def on_epoch_end(self, status):
        if dist.get_world_size() < 2 or dist.get_rank() == 0:
            mode = status['mode']
            if mode == 'eval':
                sample_num = status['sample_num']
                cost_time = status['cost_time']
                logger.info('Total sample number: {}, averge FPS: {}'.format(
                    sample_num, sample_num / cost_time))


class Checkpointer(Callback):
    def __init__(self, model):
        super(Checkpointer, self).__init__(model)
        cfg = self.model.cfg
        self.best_ap = 0.
        self.save_dir = self.model.cfg.save_dir
        if hasattr(self.model.model, 'student_model'):
            self.weight = self.model.model.student_model
        else:
            self.weight = self.model.model

    def on_epoch_end(self, status):
        # Checkpointer only performed during training
        mode = status['mode']
        epoch_id = status['epoch_id']
        weight = None
        save_name = None
        if dist.get_world_size() < 2 or dist.get_rank() == 0:
            if mode == 'train':
                # end_epoch = self.model.cfg.epoch
                # if (epoch_id + 1) % self.model.cfg.snapshot_epoch == 0 or epoch_id == end_epoch - 1:
                #     save_name = str(epoch_id) if epoch_id != end_epoch - 1 else "model_final"
                #     weight = self.weight.state_dict()
                # 不保存过程权重，只在评测阶段保存best_model，必须确保训练参数 --eval为True
                pass
            elif mode == 'eval':
                if 'save_best_model' in status and status['save_best_model']:
                    for metric in self.model._metrics:
                        map_res = metric.get_results()
                        if 'bbox' in map_res:
                            key = 'bbox'
                        elif 'keypoint' in map_res:
                            key = 'keypoint'
                        else:
                            key = 'mask'
                        if key not in map_res:
                            logger.warning("Evaluation results empty, this may be due to " \
                                        "training iterations being too few or not " \
                                        "loading the correct weights.")
                            return
                        if map_res[key][0] >= self.best_ap:
                            self.best_ap = map_res[key][0]
                            save_name = 'best_model'
                            weight = self.weight.state_dict()
                        logger.info("Best test {} ap is {:0.3f}.".format(
                            key, self.best_ap))
            if weight:
                if self.model.use_ema:
                    # save model and ema_model
                    save_model(
                        status['weight'],
                        self.model.optimizer,
                        self.save_dir,
                        save_name,
                        epoch_id + 1,
                        ema_model=weight)
                else:
                    save_model(weight, self.model.optimizer, self.save_dir,
                               save_name, epoch_id + 1)


class WiferFaceEval(Callback):
    def __init__(self, model):
        super(WiferFaceEval, self).__init__(model)

    def on_epoch_begin(self, status):
        assert self.model.mode == 'eval', \
            "WiferFaceEval can only be set during evaluation"
        for metric in self.model._metrics:
            metric.update(self.model.model)
        sys.exit()


class VisualDLWriter(Callback):
    """
    Use VisualDL to log data or image
    """

    def __init__(self, model):
        super(VisualDLWriter, self).__init__(model)

        assert six.PY3, "VisualDL requires Python >= 3.5"
        try:
            from visualdl import LogWriter
        except Exception as e:
            logger.error('visualdl not found, plaese install visualdl. '
                         'for example: `pip install visualdl`.')
            raise e
        self.vdl_writer = LogWriter(
            model.cfg.get('vdl_log_dir', 'vdl_log_dir/scalar'))
        self.vdl_loss_step = 0
        self.vdl_mAP_step = 0
        self.vdl_image_step = 0
        self.vdl_image_frame = 0

    def on_step_end(self, status):
        mode = status['mode']
        if dist.get_world_size() < 2 or dist.get_rank() == 0:
            if mode == 'train':
                training_staus = status['training_staus']
                for loss_name, loss_value in training_staus.get().items():
                    self.vdl_writer.add_scalar(loss_name, loss_value,
                                               self.vdl_loss_step)
                self.vdl_loss_step += 1
            elif mode == 'test':
                ori_image = status['original_image']
                result_image = status['result_image']
                self.vdl_writer.add_image(
                    "original/frame_{}".format(self.vdl_image_frame), ori_image,
                    self.vdl_image_step)
                self.vdl_writer.add_image(
                    "result/frame_{}".format(self.vdl_image_frame),
                    result_image, self.vdl_image_step)
                self.vdl_image_step += 1
                # each frame can display ten pictures at most.
                if self.vdl_image_step % 10 == 0:
                    self.vdl_image_step = 0
                    self.vdl_image_frame += 1

    def on_epoch_end(self, status):
        mode = status['mode']
        if dist.get_world_size() < 2 or dist.get_rank() == 0:
            if mode == 'eval':
                for metric in self.model._metrics:
                    for key, map_value in metric.get_results().items():
                        self.vdl_writer.add_scalar("{}-mAP".format(key),
                                                   map_value[0],
                                                   self.vdl_mAP_step)
                self.vdl_mAP_step += 1

class WandbCallback(Callback):
    def __init__(self, model):
        super(WandbCallback, self).__init__(model)

        try:
            import wandb
            self.wandb = wandb
        except Exception as e:
            logger.error('wandb not found, please install wandb. '
                         'Use: `pip install wandb`.')
            raise e

        self.wandb_params = model.cfg.get('wandb', None)
        self.save_dir = os.path.join(self.model.cfg.save_dir,
                                     self.model.cfg.filename)
        if self.wandb_params is None:
            self.wandb_params = {}
        for k, v in model.cfg.items():
            if k.startswith("wandb_"):
                self.wandb_params.update({
                    k.lstrip("wandb_"): v
                })
        
        self._run = None
        if dist.get_world_size() < 2 or dist.get_rank() == 0:
            _ = self.run
            self.run.config.update(self.model.cfg)
            self.run.define_metric("epoch")
            self.run.define_metric("eval/*", step_metric="epoch")

        self.best_ap = 0
    
    @property
    def run(self):
        if self._run is None:
            if self.wandb.run is not None:
                logger.info("There is an ongoing wandb run which will be used"
                        "for logging. Please use `wandb.finish()` to end that"
                        "if the behaviour is not intended")
                self._run = self.wandb.run
            else:
                self._run = self.wandb.init(**self.wandb_params)
        return self._run
    
    def save_model(self,
                optimizer,
                save_dir,
                save_name,
                last_epoch,
                ema_model=None,
                ap=None, 
                tags=None):
        if dist.get_world_size() < 2 or dist.get_rank() == 0:
            model_path = os.path.join(save_dir, save_name)
            metadata = {}
            metadata["last_epoch"] = last_epoch
            if ap:
                metadata["ap"] = ap
            if ema_model is None:
                ema_artifact = self.wandb.Artifact(name="ema_model-{}".format(self.run.id), type="model", metadata=metadata)
                model_artifact = self.wandb.Artifact(name="model-{}".format(self.run.id), type="model", metadata=metadata)

                ema_artifact.add_file(model_path + ".pdema", name="model_ema")
                model_artifact.add_file(model_path + ".pdparams", name="model")

                self.run.log_artifact(ema_artifact, aliases=tags)
                self.run.log_artfact(model_artifact, aliases=tags)
            else:
                model_artifact = self.wandb.Artifact(name="model-{}".format(self.run.id), type="model", metadata=metadata)
                model_artifact.add_file(model_path + ".pdparams", name="model")
                self.run.log_artifact(model_artifact, aliases=tags)
    
    def on_step_end(self, status):

        mode = status['mode']
        if dist.get_world_size() < 2 or dist.get_rank() == 0:
            if mode == 'train':
                training_status = status['training_staus'].get()
                for k, v in training_status.items():
                    training_status[k] = float(v)
                metrics = {
                    "train/" + k: v for k,v in training_status.items()
                }
                self.run.log(metrics)
    
    def on_epoch_end(self, status):
        mode = status['mode']
        epoch_id = status['epoch_id']
        save_name = None
        if dist.get_world_size() < 2 or dist.get_rank() == 0:
            if mode == 'train':
                end_epoch = self.model.cfg.epoch
                if (
                        epoch_id + 1
                ) % self.model.cfg.snapshot_epoch == 0 or epoch_id == end_epoch - 1:
                    save_name = str(epoch_id) if epoch_id != end_epoch - 1 else "model_final"
                    tags = ["latest", "epoch_{}".format(epoch_id)]
                    self.save_model(
                        self.model.optimizer,
                        self.save_dir,
                        save_name,
                        epoch_id + 1,
                        self.model.use_ema,
                        tags=tags
                    )
            if mode == 'eval':
                merged_dict = {}
                for metric in self.model._metrics:
                    for key, map_value in metric.get_results().items():
                        merged_dict["eval/{}-mAP".format(key)] = map_value[0]
                merged_dict["epoch"] = status["epoch_id"]
                self.run.log(merged_dict)

                if 'save_best_model' in status and status['save_best_model']:
                    for metric in self.model._metrics:
                        map_res = metric.get_results()
                        if 'bbox' in map_res:
                            key = 'bbox'
                        elif 'keypoint' in map_res:
                            key = 'keypoint'
                        else:
                            key = 'mask'
                        if key not in map_res:
                            logger.warning("Evaluation results empty, this may be due to " \
                                        "training iterations being too few or not " \
                                        "loading the correct weights.")
                            return
                        if map_res[key][0] >= self.best_ap:
                            self.best_ap = map_res[key][0]
                            save_name = 'best_model'
                            tags = ["best", "epoch_{}".format(epoch_id)]

                            self.save_model(
                                self.model.optimizer,
                                self.save_dir,
                                save_name,
                                last_epoch=epoch_id + 1,
                                ema_model=self.model.use_ema,
                                ap=self.best_ap,
                                tags=tags
                            )
    
    def on_train_end(self, status):
        self.run.finish()


class SniperProposalsGenerator(Callback):
    def __init__(self, model):
        super(SniperProposalsGenerator, self).__init__(model)
        ori_dataset = self.model.dataset
        self.dataset = self._create_new_dataset(ori_dataset)
        self.loader = self.model.loader
        self.cfg = self.model.cfg
        self.infer_model = self.model.model

    def _create_new_dataset(self, ori_dataset):
        dataset = copy.deepcopy(ori_dataset)
        # init anno_cropper
        dataset.init_anno_cropper()
        # generate infer roidbs
        ori_roidbs = dataset.get_ori_roidbs()
        roidbs = dataset.anno_cropper.crop_infer_anno_records(ori_roidbs)
        # set new roidbs
        dataset.set_roidbs(roidbs)

        return dataset

    def _eval_with_loader(self, loader):
        results = []
        with paddle.no_grad():
            self.infer_model.eval()
            for step_id, data in enumerate(loader):
                outs = self.infer_model(data)
                for key in ['im_shape', 'scale_factor', 'im_id']:
                    outs[key] = data[key]
                for key, value in outs.items():
                    if hasattr(value, 'numpy'):
                        outs[key] = value.numpy()

                results.append(outs)

        return results

    def on_train_end(self, status):
        self.loader.dataset = self.dataset
        results = self._eval_with_loader(self.loader)
        results = self.dataset.anno_cropper.aggregate_chips_detections(results)
        # sniper
        proposals = []
        clsid2catid = {v: k for k, v in self.dataset.catid2clsid.items()}
        for outs in results:
            batch_res = get_infer_results(outs, clsid2catid)
            start = 0
            for i, im_id in enumerate(outs['im_id']):
                bbox_num = outs['bbox_num']
                end = start + bbox_num[i]
                bbox_res = batch_res['bbox'][start:end] \
                    if 'bbox' in batch_res else None
                if bbox_res:
                    proposals += bbox_res
        logger.info("save proposals in {}".format(self.cfg.proposals_path))
        with open(self.cfg.proposals_path, 'w') as f:
            json.dump(proposals, f)


class MetricsTracker(Callback):
    def __init__(self, model):
        super(MetricsTracker, self).__init__(model)
        self.best_ap = 0.
        self.best_schema_metric: Optional[Dict] = None
        self.training_metric = TrainMetric(metrics=[])
        self.work_dir = os.environ.get('WINDMILL_EXPERIMENT_WORK_DIR', 
                                        os.path.join(self.model.cfg.save_dir, "wwd"))
        self.run_id = os.environ.get('WINDMILL_EXPERIMENT_RUN_ID', '100')
        self.save_dir = self.model.cfg.save_dir
        _nranks = dist.get_world_size()
        _local_rank = dist.get_rank()
        if _nranks < 2 or _local_rank == 0:
            if not os.path.exists(self.work_dir):
                os.makedirs(self.work_dir, exist_ok=True)
            if not os.path.exists(self.save_dir):
                os.makedirs(self.save_dir, exist_ok=True)

    def on_step_end(self, status):
        mode = status['mode']
        if dist.get_world_size() < 2 or dist.get_rank() == 0:
            if mode == 'train':
                epoch_id = status['epoch_id'] if 'epoch_id' in status else 0
                step = status['step_id'] + epoch_id * status['steps_per_epoch']
                self.training_metric.step = step
                self.training_metric.epoch = None
                training_staus = status['training_staus'].get()
                metric_file = os.path.join(self.work_dir, f'{self.run_id}.json')
                if 'loss' in training_staus:
                    self.training_metric.metrics = []
                    if os.path.exists(metric_file):
                        with open(metric_file, 'r', encoding='utf-8') as f:
                            try:
                                fcntl.flock(f, fcntl.LOCK_EX)
                                last_metric = json.load(f)
                            finally:
                                fcntl.flock(f, fcntl.LOCK_UN)
                        self.training_metric.epoch = last_metric['epoch']
                        for metric in last_metric['metrics']:
                            if metric['name'] != 'Loss':
                                self.training_metric.metrics.append(BaseTrainMetric(name=metric['name'],
                                                                                    result=metric['result']))
                    self.training_metric.metrics.append(BaseTrainMetric(name="Loss", result=training_staus['loss']))
                    with open(metric_file, 'w', encoding='utf-8') as f:
                        try:
                            fcntl.flock(f, fcntl.LOCK_EX)
                            json.dump(self.training_metric.dict(), f, indent=2, ensure_ascii=False)
                        finally:
                            fcntl.flock(f, fcntl.LOCK_UN)
                    logger.info(f"Save training loss to {self.work_dir}/{self.run_id}.json on step {step}")
    
    def on_epoch_end(self, status):
        mode = status['mode']
        if dist.get_world_size() < 2 or dist.get_rank() == 0:
            if mode == 'train':
                epoch_id = status['epoch_id']
                self.training_metric.epoch = epoch_id
                self.training_metric.step = None
                for metric in self.model._metrics:
                    map_res = metric.get_results()
                    if 'bbox' in map_res:
                        key = 'bbox'
                    elif 'keypoint' in map_res:
                        key = 'keypoint'
                    else:
                        continue
                    curr_epoch_metric = map_res["GAEA_TRACKER_METRICS"]['schema'] \
                                            if "GAEA_TRACKER_METRICS" in map_res else None
                    if map_res[key][0] >= self.best_ap:
                        self.best_ap = map_res[key][0]
                        if curr_epoch_metric is not None:
                            self.best_schema_metric = curr_epoch_metric
                    # 训练过程中指标保存到work_dir
                    curr_train_metric = map_res["GAEA_TRACKER_METRICS"]['train_schema'] \
                                            if "GAEA_TRACKER_METRICS" in map_res else None
                    metric_file = os.path.join(self.work_dir, f'{self.run_id}.json')
                    if curr_train_metric is not None:
                        self.training_metric.metrics = []
                        if os.path.exists(metric_file):
                            with open(metric_file, 'r', encoding='utf-8') as f:
                                try:
                                    fcntl.flock(f, fcntl.LOCK_EX)
                                    last_metric = json.load(f)
                                finally:
                                    fcntl.flock(f, fcntl.LOCK_UN)
                            self.training_metric.step = last_metric['step']
                            for sub_metric in last_metric['metrics']:
                                if sub_metric['name'] == 'Loss':
                                    self.training_metric.metrics.append(BaseTrainMetric(name=sub_metric['name'],
                                                                                        result=sub_metric['result']))

                        for metric in curr_train_metric["metrics"]:
                            self.training_metric.metrics.append(BaseTrainMetric(name=metric["name"],
                                                                                result=metric["result"]))
                        with open(os.path.join(self.work_dir, f'{self.run_id}.json'), 'w', encoding='utf-8') as f:
                            try:
                                fcntl.flock(f, fcntl.LOCK_EX)
                                json.dump(self.training_metric.dict(), f, indent=2, ensure_ascii=False)
                            finally:
                                fcntl.flock(f, fcntl.LOCK_UN)
                        logger.info(f"Save training metric to {self.work_dir}/{self.run_id}.json on epoch {epoch_id}")

            elif mode == 'eval':
                for metric in self.model._metrics:
                    map_res = metric.get_results()
                    if "GAEA_TRACKER_METRICS" in map_res:
                        self.best_schema_metric = map_res["GAEA_TRACKER_METRICS"]['schema']
                        with open(os.path.join(self.save_dir, 'metric.json'), 'w', encoding='utf-8') as f:
                            try:
                                fcntl.flock(f, fcntl.LOCK_EX)
                                json.dump(self.best_schema_metric, f, indent=2, ensure_ascii=False)
                            finally:
                                fcntl.flock(f, fcntl.LOCK_UN)
                            
                        with open(os.path.join(self.work_dir, 'metric.json'), 'w', encoding='utf-8') as f:
                            try:
                                fcntl.flock(f, fcntl.LOCK_EX)
                                json.dump(self.best_schema_metric, f, indent=2, ensure_ascii=False)
                            finally:
                                fcntl.flock(f, fcntl.LOCK_UN)
                        logger.info(f"[EVAL] Save metric to {self.work_dir}/metric.json")
                        logger.info(f"[EVAL] Save metric to {self.save_dir}/metric.json")

    def on_train_end(self, status):
        if dist.get_world_size() < 2 or dist.get_rank() == 0:
            if self.best_schema_metric is not None:
                with open(os.path.join(self.save_dir, 'metric.json'), 'w', encoding='utf-8') as f:
                    try:
                        fcntl.flock(f, fcntl.LOCK_EX)
                        json.dump(self.best_schema_metric, f, indent=2, ensure_ascii=False)
                    finally:
                        fcntl.flock(f, fcntl.LOCK_UN)
                    
                with open(os.path.join(self.work_dir, 'metric.json'), 'w', encoding='utf-8') as f:
                    try:
                        fcntl.flock(f, fcntl.LOCK_EX)
                        json.dump(self.best_schema_metric, f, indent=2, ensure_ascii=False)
                    finally:
                        fcntl.flock(f, fcntl.LOCK_UN)
                logger.info(f"Save best metric to {self.work_dir}/metric.json")
                logger.info(f"Save best metric to {self.save_dir}/metric.json")