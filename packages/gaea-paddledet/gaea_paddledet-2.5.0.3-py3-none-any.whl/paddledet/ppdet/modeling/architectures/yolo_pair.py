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

import paddle
import paddle.nn as nn
from paddle import ParamAttr
from paddle.regularizer import L2Decay
import paddle.nn.functional as F
from ppdet.modeling.ops import get_act_fn
from ppdet.modeling.initializer import conv_init_
from ppdet.core.workspace import register, create
from .meta_arch_pair import BaseArchPair
from ..post_process import JDEBBoxPostProcess

__all__ = ['YOLOv3Pair']


class ConvBNLayerPair(nn.Layer):
    def __init__(self,
                 ch_in,
                 ch_out,
                 filter_size=3,
                 stride=1,
                 groups=1,
                 padding=0,
                 act=None):
        super(ConvBNLayerPair, self).__init__()

        self.conv = nn.Conv2D(
            in_channels=ch_in,
            out_channels=ch_out,
            kernel_size=filter_size,
            stride=stride,
            padding=padding,
            groups=groups,
            bias_attr=False)

        self.bn = nn.BatchNorm2D(
            ch_out,
            weight_attr=ParamAttr(regularizer=L2Decay(0.0)),
            bias_attr=ParamAttr(regularizer=L2Decay(0.0)))
        self.act = get_act_fn(act) if act is None or isinstance(act, (
            str, dict)) else act

    def forward(self, x):
        x = self.conv(x)
        x = self.bn(x)
        x = self.act(x)

        return x


class Scale(nn.Layer):
    """
    自学习单缩放参数 scale_a scale_b
    """
    def __init__(self, scale=1.0):
        super(Scale, self).__init__()
        self.scale = paddle.static.create_parameter(shape=[1], dtype='float32', 
        default_initializer=nn.initializer.Constant(value=scale))

    def forward(self, x):
        return x * self.scale

class ScaleChannel(nn.Layer):
    """
    分特征通道学习缩放参数 scale_a scale_b
    """
    def __init__(self, scale=1.0, channels=[144, 288, 576]):
        super(ScaleChannel, self).__init__()
        # self.scale = nn.Parameter(torch.ones(channels, dtype=torch.float)*scale)
        self.scale_large = paddle.static.create_parameter(shape=[channels[2]], dtype='float32',
        default_initializer=nn.initializer.Constant(value=scale))
        self.scale_medium = paddle.static.create_parameter(shape=[channels[1]], dtype='float32',
        default_initializer=nn.initializer.Constant(value=scale))
        self.scale_small = paddle.static.create_parameter(shape=[channels[0]], dtype='float32',
        default_initializer=nn.initializer.Constant(value=scale))

    def forward(self, x):
        b, c, h, w = x.shape
        if c == 576:
            out = x.reshape([b, c, -1]) * self.scale_large.reshape([-1, 1])
            out = out.reshape([b, c, h, w])
        elif c == 288:
            out = x.reshape([b, c, -1]) * self.scale_medium.reshape([-1, 1])
            out = out.reshape([b, c, h, w])
        elif c == 144:
            out = x.reshape([b, c, -1]) * self.scale_small.reshape([-1, 1])
            out = out.reshape([b, c, h, w])
        else:
            print(f"x.shape:{x.shape}")
        return out

class ScaleConv(nn.Layer):
    """
    1*1卷积得到out_channels减半的两组特征，再通过concat合并
    """
    def __init__(self, in_channels, out_channels):
        super(ScaleConv, self).__init__()
        self.scale_large = ConvBNLayerPair(
            in_channels[2],
            out_channels[2],
            filter_size=1,
            stride=1,
            groups=1,
            act="swish")

        self.scale_medium = ConvBNLayerPair(
            in_channels[1],
            out_channels[1],
            filter_size=1,
            stride=1,
            groups=1,
            act="swish")

        self.scale_small = ConvBNLayerPair(
            in_channels[0],
            out_channels[0],
            filter_size=1,
            stride=1,
            groups=1,
            act="swish")

    def forward(self, x):
        b, c, h, w = x.shape
        if c == 576:
            out = self.scale_large(x)
        elif c == 288:
            out = self.scale_medium(x)
        elif c == 144:
            out = self.scale_small(x)
        else:
            print(f"x.shape:{x.shape}")
        return out




@register
class YOLOv3Pair(BaseArchPair):
    __category__ = 'architecture'
    __shared__ = ['data_format']
    __inject__ = ['post_process']

    def __init__(self,
                 backbone='CSPResNetPair',
                 neck='CustomCSPPAN',
                 yolo_head='PPYOLOEHead',
                 post_process='BBoxPostProcess',
                 data_format='NCHW',
                 scale_style='scale',
                 for_mot=False):
        """
        YOLOv3 network, see https://arxiv.org/abs/1804.02767

        Args:
            backbone (nn.Layer): backbone instance
            neck (nn.Layer): neck instance
            yolo_head (nn.Layer): anchor_head instance
            bbox_post_process (object): `BBoxPostProcess` instance
            data_format (str): data format, NCHW or NHWC
            for_mot (bool): whether return other features for multi-object tracking
                models, default False in pure object detection models.
        """
        super(YOLOv3Pair, self).__init__(data_format=data_format)
        self.backbone = backbone
        self.neck = neck
        self.yolo_head = yolo_head
        self.post_process = post_process
        self.for_mot = for_mot
        self.return_idx = isinstance(post_process, JDEBBoxPostProcess)
        self.scale_style = scale_style
        print(f"scale_style:{self.scale_style}")

        if self.scale_style == 'scale':
            self.scale_a = Scale(0.5)
            self.scale_b = Scale(0.5)
        elif self.scale_style == 'scale_channel':
            self.scale_a = ScaleChannel(scale=0.5, channels=[144, 288, 576])
            self.scale_b = ScaleChannel(scale=0.5, channels=[144, 288, 576])
        elif self.scale_style == 'scale_conv':
            self.scale_a = ScaleConv(in_channels=[144, 288, 576], out_channels=[72, 144, 288])
            self.scale_b = ScaleConv(in_channels=[144, 288, 576], out_channels=[72, 144, 288])
        elif self.scale_style == 'diff':
            pass
        elif self.scale_style == 'abs_diff':
            pass
        elif self.scale_style == 'sum':
            pass
        else:
            raise ValueError('invalid scale style')

    @classmethod
    def from_config(cls, cfg, *args, **kwargs):
        # backbone
        backbone = create(cfg['backbone'])

        # fpn
        kwargs = {'input_shape': backbone.out_shape}
        neck = create(cfg['neck'], **kwargs)

        # head
        kwargs = {'input_shape': neck.out_shape}
        yolo_head = create(cfg['yolo_head'], **kwargs)

        return {
            'backbone': backbone,
            'neck': neck,
            "yolo_head": yolo_head,
        }

    def _forward(self):
        body_feats = self.backbone(self.inputs)
        # print(f"body_feats[0].shape:{body_feats[0].shape}")
        # print(f"body_feats[1].shape:{body_feats[1].shape}")
        # print(f"body_feats[2].shape:{body_feats[2].shape}")
        neck_feats = self.neck(body_feats, self.for_mot)

        if isinstance(neck_feats, dict):
            assert self.for_mot == True
            emb_feats = neck_feats['emb_feats']
            neck_feats = neck_feats['yolo_feats']

        scale_neck_feats = []
        for i, lvl_feat in enumerate(neck_feats):
            if self.scale_style == 'scale':
                # print(f"len(lvl_feat):{lvl_feat.shape}")
                scale_neck_feats.append(self.scale_a(lvl_feat[:lvl_feat.shape[0]//2, :, :, :]) + self.scale_b(lvl_feat[lvl_feat.shape[0]//2:, :, :, :]))
            elif self.scale_style == 'scale_channel':
                scale_neck_feats.append(self.scale_a(lvl_feat[:lvl_feat.shape[0]//2, :, :, :]) + self.scale_b(lvl_feat[lvl_feat.shape[0]//2:, :, :, :]))
            elif self.scale_style == 'scale_conv':
                x_a = self.scale_a(lvl_feat[:lvl_feat.shape[0]//2, :, :, :])
                x_b = self.scale_b(lvl_feat[lvl_feat.shape[0]//2:, :, :, :])
                x_concat = paddle.concat([x_a, x_b], 1)
                scale_neck_feats.append(x_concat)
            elif self.scale_style == 'diff':
                scale_neck_feats.append(lvl_feat[:lvl_feat.shape[0]//2, :, :, :] - lvl_feat[lvl_feat.shape[0]//2:, :, :, :])
            elif self.scale_style == 'abs_diff':
                scale_neck_feats.append(paddle.abs(lvl_feat[:lvl_feat.shape[0]//2, :, :, :] - lvl_feat[lvl_feat.shape[0]//2:, :, :, :]))
            elif self.scale_style == 'sum':
                scale_neck_feats.append(lvl_feat[:lvl_feat.shape[0]//2, :, :, :] + lvl_feat[lvl_feat.shape[0]//2:, :, :, :])
            else:
                raise ValueError('unvalid scale style')



        if self.training:
            # print(f"scale_neck_feats[0].shape:{scale_neck_feats[0].shape}")
            # print(f"scale_neck_feats[1].shape:{scale_neck_feats[1].shape}")
            # print(f"scale_neck_feats[2].shape:{scale_neck_feats[2].shape}")
            # print(f"self.inputs.shape:{self.inputs}")
            yolo_losses = self.yolo_head(scale_neck_feats, self.inputs)

            if self.for_mot:
                return {'det_losses': yolo_losses, 'emb_feats': emb_feats}
            else:
                return yolo_losses

        else:
            yolo_head_outs = self.yolo_head(scale_neck_feats)

            if self.for_mot:
                boxes_idx, bbox, bbox_num, nms_keep_idx = self.post_process(
                    yolo_head_outs, self.yolo_head.mask_anchors)
                output = {
                    'bbox': bbox,
                    'bbox_num': bbox_num,
                    'boxes_idx': boxes_idx,
                    'nms_keep_idx': nms_keep_idx,
                    'emb_feats': emb_feats,
                }
            else:
                if self.return_idx:
                    _, bbox, bbox_num, _ = self.post_process(
                        yolo_head_outs, self.yolo_head.mask_anchors)
                elif self.post_process is not None:
                    bbox, bbox_num = self.post_process(
                        yolo_head_outs, self.yolo_head.mask_anchors,
                        self.inputs['im_shape'], self.inputs['scale_factor'])
                else:
                    bbox, bbox_num = self.yolo_head.post_process(
                        yolo_head_outs, self.inputs['scale_factor'])
                output = {'bbox': bbox, 'bbox_num': bbox_num}

            return output

    def get_loss(self):
        return self._forward()

    def get_pred(self):
        return self._forward()
