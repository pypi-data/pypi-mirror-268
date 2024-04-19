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
from re import M
import sys
import numpy as np
import itertools

from ppdet.metrics.json_results import get_det_res, get_det_poly_res, get_seg_res, get_solov2_segm_res, get_keypoint_res
from ppdet.metrics.map_utils import draw_pr_curve
#from ppdet.utils.object_detection_metric_api import *
from gaea_operator.metric.types.object_detection_metric import TrainMetric, BaseTrainMetric, \
    BoundingBoxLabelAveragePrecision, BoundingBoxLabelAveragePrecision, ObjectDetectionMetric, \
    BoundingBoxMeanAveragePrecision, BoundingBoxLabelMetric, BoundingBoxMeanAverageRecall, \
    BoundingBoxLabelAveragePrecisionResult, BoundingBoxLabelConfidenceMetric, BoundingBoxLabelMetricResult, Label
from gaea_operator.metric.types.metric import ConfusionMatrixMetric, \
    ConfusionMatrixMetricResult, \
    ConfusionMatrixRow, \
    ConfusionMatrixAnnotationSpec
from collections import defaultdict
import copy
from pycocotools import mask as mask_utils
from pycocotools.coco import COCO
from ppdet.utils.logger import setup_logger
logger = setup_logger(__name__)


def get_infer_results(outs, catid, bias=0):
    """
    Get result at the stage of inference.
    The output format is dictionary containing bbox or mask result.

    For example, bbox result is a list and each element contains
    image_id, category_id, bbox and score.
    """
    if outs is None or len(outs) == 0:
        raise ValueError(
            'The number of valid detection result if zero. Please use reasonable model and check input data.'
        )

    im_id = outs['im_id']

    infer_res = {}
    if 'bbox' in outs:
        if len(outs['bbox']) > 0 and len(outs['bbox'][0]) > 6:
            infer_res['bbox'] = get_det_poly_res(
                outs['bbox'], outs['bbox_num'], im_id, catid, bias=bias)
        else:
            infer_res['bbox'] = get_det_res(
                outs['bbox'], outs['bbox_num'], im_id, catid, bias=bias)

    if 'mask' in outs:
        # mask post process
        infer_res['mask'] = get_seg_res(outs['mask'], outs['bbox'],
                                        outs['bbox_num'], im_id, catid)

    if 'segm' in outs:
        infer_res['segm'] = get_solov2_segm_res(outs, im_id, catid)

    if 'keypoint' in outs:
        infer_res['keypoint'] = get_keypoint_res(outs, im_id)
        outs['bbox_num'] = [len(infer_res['keypoint'])]

    return infer_res


def cocoapi_eval(jsonfile,
                 style,
                 coco_gt=None,
                 anno_file=None,
                 max_dets=(100, 300, 1000),
                 classwise=False,
                 sigmas=None,
                 use_area=True):
    """
    Args:
        jsonfile (str): Evaluation json file, eg: bbox.json, mask.json.
        style (str): COCOeval style, can be `bbox` , `segm` , `proposal`, `keypoints` and `keypoints_crowd`.
        coco_gt (str): Whether to load COCOAPI through anno_file,
                 eg: coco_gt = COCO(anno_file)
        anno_file (str): COCO annotations file.
        max_dets (tuple): COCO evaluation maxDets.
        classwise (bool): Whether per-category AP and draw P-R Curve or not.
        sigmas (nparray): keypoint labelling sigmas.
        use_area (bool): If gt annotations (eg. CrowdPose, AIC)
                         do not have 'area', please set use_area=False.
    """
    assert coco_gt is not None or anno_file is not None
    if style == 'keypoints_crowd':
        #please install xtcocotools==1.6
        from xtcocotools.coco import COCO
        from xtcocotools.cocoeval import COCOeval
    else:
        from pycocotools.coco import COCO
        from pycocotools.cocoeval import COCOeval

    if coco_gt is None:
        coco_gt = COCO(anno_file)
    logger.info("Start evaluate...")
    coco_dt = coco_gt.loadRes(jsonfile)
    if style == 'proposal':
        coco_eval = COCOeval(coco_gt, coco_dt, 'bbox')
        coco_eval.params.useCats = 0
        coco_eval.params.maxDets = list(max_dets)
    elif style == 'keypoints_crowd':
        coco_eval = COCOeval(coco_gt, coco_dt, style, sigmas, use_area)
    else:
        coco_eval = COCOeval(coco_gt, coco_dt, style)
    coco_eval.evaluate()
    coco_eval.accumulate()
    coco_eval.summarize()
    if classwise:
        # Compute per-category AP and PR curve
        try:
            from terminaltables import AsciiTable
        except Exception as e:
            logger.error(
                'terminaltables not found, plaese install terminaltables. '
                'for example: `pip install terminaltables`.')
            raise e
        precisions = coco_eval.eval['precision']
        cat_ids = coco_gt.getCatIds()
        # precision: (iou, recall, cls, area range, max dets)
        assert len(cat_ids) == precisions.shape[2]
        results_per_category = []
        for idx, catId in enumerate(cat_ids):
            # area range index 0: all area ranges
            # max dets index -1: typically 100 per image
            nm = coco_gt.loadCats(catId)[0]
            precision = precisions[:, :, idx, 0, -1]
            precision = precision[precision > -1]
            if precision.size:
                ap = np.mean(precision)
            else:
                ap = -1.0 # float('nan')
            results_per_category.append(
                (str(nm["name"]), '{:0.3f}'.format(float(ap))))
            pr_array = precisions[0, :, idx, 0, 2]
            recall_array = np.arange(0.0, 1.01, 0.01)
            draw_pr_curve(
                pr_array,
                recall_array,
                out_dir=style + '_pr_curve',
                file_name='{}_precision_recall_curve.jpg'.format(nm["name"]))

        num_columns = min(6, len(results_per_category) * 2)
        results_flatten = list(itertools.chain(*results_per_category))
        headers = ['category', 'AP'] * (num_columns // 2)
        results_2d = itertools.zip_longest(
            *[results_flatten[i::num_columns] for i in range(num_columns)])
        table_data = [headers]
        table_data += [result for result in results_2d]
        table = AsciiTable(table_data)
        logger.info('Per-category of {} AP: \n{}'.format(style, table.table))
        logger.info("per-category PR curve has output to {} folder.".format(
            style + '_pr_curve'))
    # flush coco evaluation result
    sys.stdout.flush()
    return coco_eval.stats


def cocoapi_detail_eval(jsonfile,
                        style,
                        coco_gt=None,
                        anno_file=None,
                        max_dets=(100, 300, 1000),
                        sigmas=None,
                        use_area=True,
                        iou_thrs=0.5,
                        score_thrs=0.5,
                        draw_PR_curve=False,
                        confusion_matrix=False,):
    """
    Args:
        jsonfile (str): Evaluation json file, eg: bbox.json, mask.json.
        style (str): COCOeval style, can be `bbox` , `segm` , `proposal`, `keypoints` and `keypoints_crowd`.
        coco_gt (str): Whether to load COCOAPI through anno_file,
                 eg: coco_gt = COCO(anno_file)
        anno_file (str): COCO annotations file.
        max_dets (tuple): COCO evaluation maxDets.
        sigmas (nparray): keypoint labelling sigmas.
        use_area (bool): If gt annotations (eg. CrowdPose, AIC)
                         do not have 'area', please set use_area=False.
    """
    assert coco_gt != None or anno_file != None
    if style == 'keypoints_crowd':
        #please install xtcocotools==1.6
        from xtcocotools.coco import COCO
        from xtcocotools.cocoeval import COCOeval
    else:
        from pycocotools.coco import COCO
        from pycocotools.cocoeval import COCOeval

    if coco_gt == None:
        coco_gt = COCO(anno_file)
    coco_dt = coco_gt.loadRes(jsonfile)
    if style == 'proposal':
        coco_eval = COCOeval(coco_gt, coco_dt, 'bbox')
        coco_eval.params.useCats = 0
        coco_eval.params.maxDets = list(max_dets)
    elif style == 'keypoints_crowd':
        coco_eval = COCOeval(coco_gt, coco_dt, style, sigmas, use_area)
    else:
        coco_eval = COCOeval(coco_gt, coco_dt, style)
    coco_eval.evaluate()
    coco_eval.accumulate()
    coco_eval.summarize()

    coco_iouThrs = [round(i * 0.01, 2) for i in range(50, 100, 5)]  # iouThr (0.5:0.05:0.95)
    if iou_thrs not in coco_iouThrs:
        iou_thrs = 0.5
        iou_index = 0
    else:
        iou_index = coco_iouThrs.index(iou_thrs)
    # Compute per-category AP and PR curve
    precisions = coco_eval.eval['precision']
    recalls = coco_eval.eval['recall'] # iou*class_num*Areas*Max_det TP/(TP+FN) right/gt
    cat_ids = coco_gt.getCatIds()
    # precision: (iou, recall, cat, area_range, max_dets)
    # recall: (iou, cat, area_range, max_dets)
    assert len(cat_ids) == precisions.shape[2]
    results_per_category = []
    results_per_category_iou = []
    metrics = dict()
    metrics['PR'] = []
    for idx, catId in enumerate(cat_ids):
        # area range index 0: all area ranges
        # max dets index -1: typically 100 per image
        nm = coco_gt.loadCats(catId)[0]
        precision = precisions[:, :, idx, 0, -1]
        precision_iou = precisions[iou_index, :, idx, 0, -1]
        precision = precision[precision > -1]

        recall = recalls[:, idx, 0, -1]
        recall_iou = recalls[iou_index, idx, 0, -1]
        recall = recall[recall > -1]
        
        if precision.size:
            ap = np.mean(precision)
            ap_iou = np.mean(precision_iou)
            rec = np.mean(recall)
            rec_iou = np.mean(recall_iou)
        else:
            ap = -1.0 # float('nan')
            ap_iou = -1.0 # float('nan')
            rec = -1.0 # float('nan')
            rec_iou = -1.0 # float('nan')
        res_item = [str(nm["name"]), catId, round(float(ap), 4), round(float(rec), 4)]  # name, cat_id, ap, ar
        results_per_category.append(res_item)
        res_item_iou = [str(nm["name"]), catId, round(float(ap_iou), 4), round(float(rec_iou), 4)]
        results_per_category_iou.append(res_item_iou)
        
        metrics['PR'].append([str(nm["name"]), catId, list(precision_iou), 
            [round(i * 0.01, 2) for i in range(101)]])

    # if confusion_matrix:
    cm, cat_id2index = compute_confusion_matrix(coco_gt, coco_dt, score_thrs, iou_thrs)
    print("Confusion Matrix is: \n {}".format(cm))
    metrics['ConfusionMatrix'] = cm
    
    bbox_stats = coco_eval.stats
    # 总平均指标
    metrics['mAP'] = bbox_stats[0]
    metrics['mAR'] = bbox_stats[8]
    # 某一IOU阈值下的平均指标
    per_cat_ap_iou = np.array([res_item_iou[2] for res_item_iou in results_per_category_iou], dtype=float)
    mAP_iou = np.mean(per_cat_ap_iou[per_cat_ap_iou >= 0.]) # 忽略掉由Nan替换为-1的数值
    per_cat_ar_iou = np.array([res_item_iou[3] for res_item_iou in results_per_category_iou], dtype=float)
    mAR_iou = np.mean(per_cat_ar_iou[per_cat_ar_iou >= 0.])
    metrics['mAP_iou'] = round(mAP_iou, 4)
    metrics['mAR_iou'] = round(mAR_iou, 4)
    # 训练过程指标
    train_metric = TrainMetric(metrics=[])
    train_metric.metrics.append(BaseTrainMetric(name="mAP", result=metrics['mAP']))
    train_metric.metrics.append(BaseTrainMetric(name="AP50", result=metrics['mAP_iou']))
    train_metric.metrics.append(BaseTrainMetric(name="AR", result=metrics['mAR']))

    # 结果指标
    # det_metric_schema = {"metrics": []}
    schema_metric = ObjectDetectionMetric()
    schema_metric.labels = []
    schema_metric.metrics = []
    # boundingBoxMeanAveragePrecision
    bbox_mean_ap = BoundingBoxMeanAveragePrecision(
                    name="boundingBoxMeanAveragePrecision",
                    displayName="AP50指标", 
                    result=metrics['mAP_iou'])

    # boundingBoxMeanAverageRecall
    bbox_mean_ar = BoundingBoxMeanAverageRecall(name="boundingBoxMeanAverageRecall",
                    displayName="AR指标",
                    result=metrics['mAR'])


    # boundingBoxCategoryAveragePrecision
    bbox_cat_ap = BoundingBoxLabelAveragePrecision(
                    name="boundingBoxLabelAveragePrecision",
                    displayName="类别AP结果", 
                    result=[])
    # pr
    PR_curve = BoundingBoxLabelMetric(name="boundingBoxLabelMetric",
                displayName= "P-R曲线",
                result=[])

    # ConfusionMatrix
    confusion_matrix = ConfusionMatrixMetric(name="confusionMatrix",
                        displayName="混淆矩阵", 
                        result=ConfusionMatrixMetricResult(annotationSpecs=[], rows=[],
                                lowerBound=cm.min(), upperBound=cm.max()))

    for i, res_cat_item in enumerate(results_per_category):
  
        bbox_cat_ap.result.append(BoundingBoxLabelAveragePrecisionResult(
                                    labelName=res_cat_item[0],   
                                    averagePrecision=res_cat_item[2]))
        confidence_metrics = []
        per_cat_item_ps = metrics['PR'][i][2]
        per_cat_item_rs = metrics['PR'][i][3]
        for p, r in zip(per_cat_item_ps, per_cat_item_rs):
            confidence_metrics.append(BoundingBoxLabelConfidenceMetric(precision=p, recall=r))
        PR_curve.result.append(BoundingBoxLabelMetricResult(
                                labelName=res_cat_item[0],
                                iouThreshold=iou_thrs,
                                averagePrecision=results_per_category_iou[i][2],
                                confidenceMetrics=confidence_metrics))

        cat_id = int(res_cat_item[1])
        ind = cat_id2index[cat_id]
        confusion_matrix.result.annotationSpecs.append(ConfusionMatrixAnnotationSpec(
                                                        labelName=res_cat_item[0], id=cat_id))
        confusion_matrix.result.rows.append(ConfusionMatrixRow(
                                            row=metrics['ConfusionMatrix'][ind].tolist()))

        cat_name = res_cat_item[0]
        schema_metric.labels.append(Label(name=cat_name, id=cat_id))
    # 将最后一行加入到混淆矩阵中
    confusion_matrix.result.rows.append(ConfusionMatrixRow(
                                        row=metrics['ConfusionMatrix'][-1].tolist()))
    confusion_matrix.result.annotationSpecs.append(ConfusionMatrixAnnotationSpec(
                                                    labelName="背景图", id=max(cat_ids)+1))

    schema_metric.metrics.append(PR_curve)
    schema_metric.metrics.append(bbox_mean_ap)
    schema_metric.metrics.append(bbox_mean_ar)
    schema_metric.metrics.append(bbox_cat_ap)
    schema_metric.metrics.append(confusion_matrix)
    metrics['schema'] = schema_metric.dict()
    metrics['train_schema'] = train_metric.dict()
    return metrics, bbox_stats


def json_eval_results(metric, json_directory, dataset):
    """
    cocoapi eval with already exists proposal.json, bbox.json or mask.json
    """
    assert metric == 'COCO'
    anno_file = dataset.get_anno()
    json_file_list = ['proposal.json', 'bbox.json', 'mask.json']
    if json_directory:
        assert os.path.exists(
            json_directory), "The json directory:{} does not exist".format(
                json_directory)
        for k, v in enumerate(json_file_list):
            json_file_list[k] = os.path.join(str(json_directory), v)

    coco_eval_style = ['proposal', 'bbox', 'segm']
    for i, v_json in enumerate(json_file_list):
        if os.path.exists(v_json):
            # cocoapi_eval(v_json, coco_eval_style[i], anno_file=anno_file)
            cocoapi_detail_eval(v_json, coco_eval_style[i], anno_file=anno_file, confusion_matrix=True)
        else:
            logger.info("{} not exists!".format(v_json))


def compute_confusion_matrix(coco_gt: COCO, coco_dt: COCO, conf_threshold: float = 0, iou_threshold: float = 0.5):
    """
    compute confusion matrix for each class.
    Args:
        coco_gt (pycocotools COCO): ground truth annotations in COCO format.
        coco_dt (pycocotools COCO): detected results in COCO format.
    Returns:
        confusion_matrix (list[np.ndarray]): confusion matrix of each class.
    """
    groundths = coco_gt.loadAnns(coco_gt.getAnnIds())
    predictions = coco_dt.loadAnns(coco_dt.getAnnIds())
    labels = coco_gt.getCatIds()
    num_classes = len(labels)
    label_id2index = {label: index for index, label in enumerate(labels)}
    img_ids = set()
    _dts = defaultdict(list)
    _gts = defaultdict(list)

    gts = copy.deepcopy(groundths)
    for gt in gts:
        if gt["image_id"] not in img_ids:
            img_ids.add(gt["image_id"])
        if 'bbox' in gt:
            _gts[(gt['image_id'])].append(gt)

    for pred in predictions:
        if pred["image_id"] not in img_ids:
            img_ids.add(pred["image_id"])
        _dts[(pred["image_id"])].append(pred)

    confusion_matrix = np.zeros(shape=(num_classes+1, num_classes+1), dtype=np.int64)
    for img_id in img_ids:
        gt = _gts[img_id]
        dt = _dts[img_id]
        dt = [d for d in dt if d['score'] > conf_threshold]

        if len(gt) == 0 and len(dt) == 0:
            confusion_matrix[num_classes, num_classes] += 1
        elif len(gt) == 0 and len(dt) > 0:
            for d in dt:
                confusion_matrix[num_classes, label_id2index[d['category_id']]] += 1
        elif len(gt) > 0 and len(dt) == 0:
            for g in gt:
                confusion_matrix[label_id2index[g['category_id']], num_classes] += 1
        else:
            gt_box = [g['bbox'] for g in gt]
            dt_box = [d['bbox'] for d in dt]

            iscrowd = [int(o['iscrowd']) if 'iscrowd' in o else 0 for o in gt]
            ious = mask_utils.iou(dt_box, gt_box, iscrowd)

            gtind = np.argsort([g['ignore'] if 'ignore' in g else 0 for g in gt], kind='mergesort')
            gt = [gt[i] for i in gtind]
            dtind = np.argsort([-d['score'] for d in dt], kind='mergesort')
            dt = [dt[i] for i in dtind]

            iscrowd = [int(o['iscrowd']) if 'iscrowd' in o else 0 for o in gt]
            gtIg = np.array([g['ignore'] if 'ignore' in g else 0 for g in gt])
            gt_matched_index = np.ones(len(gt)) * -1
            for dind, d in enumerate(dt):
                m = -1
                label_m = -1
                for gind, g in enumerate(gt):
                    if gt_matched_index[gind] > 0 and not iscrowd[gind]:
                        continue
                    # if dt matched to reg gt, and on ignore gt, stop
                    # 如果之前已经匹配上了一个非ignore的GT，并且当前的GT是ignore的，则跳过
                    # 匹配的情况有两种可能，类别相同(label_m不为-1)，或者类别不同
                    if m > -1 and gtIg[m] == 0 and gtIg[gind] == 1:
                        break
                    # continue to next gt unless better match made
                    if ious[dind, gind] < iou_threshold:
                        continue
                    m = gind
                    if d["category_id"] == g["category_id"]:
                        label_m = gind
                if label_m != -1:
                    gt_matched_index[label_m] = label_m
                    index = label_id2index[g["category_id"]]
                    confusion_matrix[index, index] += 1
                if m != -1 and label_m < 0:
                    gt_matched_index[m] = m
                    g_index = label_id2index[g["category_id"]]
                    d_index = label_id2index[d["category_id"]]
                    confusion_matrix[g_index, d_index] += 1
                if m == -1:
                    d_index = label_id2index[d["category_id"]]
                    confusion_matrix[num_classes, d_index] += 1

            gt_matched_index = set(np.asarray(gt_matched_index, dtype=np.int32))
            for gind, g in enumerate(gt):
                if gind not in gt_matched_index:
                    g_index = label_id2index[g["category_id"]]
                    confusion_matrix[g_index, num_classes] += 1

    return confusion_matrix, label_id2index