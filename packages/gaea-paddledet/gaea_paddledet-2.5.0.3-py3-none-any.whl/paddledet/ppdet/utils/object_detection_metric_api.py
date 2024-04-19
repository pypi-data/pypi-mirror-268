#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# @Time    : 2024/3/14
# @Author  : yanxiaodong
# @File    : metric_api.py
"""
from typing import List, Union, Optional, Dict
from pydantic import BaseModel


class Label(BaseModel):
    """
    Labeled Object
    """
    id: int
    name: str


class BoundingBoxLabelConfidenceMetric(BaseModel):
    """
    Bounding Box Label Metric
    """
    recall: Optional[float] = None
    precision: Optional[float] = None


class BoundingBoxLabelMetricResult(BaseModel):
    """
    Bounding Box Label Metric
    """
    labelName: Optional[str] = None
    iouThreshold: Optional[float] = None
    averagePrecision: Optional[float] = None
    confidenceMetrics: Optional[List[BoundingBoxLabelConfidenceMetric]] = None


class BoundingBoxLabelMetric(BaseModel):
    """
    Bounding Box Label Metric
    """
    name: Optional[str] = None
    displayName: Optional[str] = None
    result: Optional[List[BoundingBoxLabelMetricResult]] = None


class BoundingBoxMeanAveragePrecisionResult(BaseModel):
    """
    Bounding Box Mean Average Precision Metric
    """
    meanAveragePrecision: Optional[float] = None


class BoundingBoxMeanAveragePrecision(BaseModel):
    """
    Bounding Box Mean Average Precision Metric
    """
    name: Optional[str] = None
    displayName: Optional[str] = None
    result: Optional[float] = None


class BoundingBoxMeanAverageRecallResult(BaseModel):
    """
    Bounding Box Mean Average Precision Metric
    """
    meanAverageRecall: Optional[float] = None


class BoundingBoxMeanAverageRecall(BaseModel):
    """
    Bounding Box Mean Average Recall Metric
    """
    name: Optional[str] = None
    displayName: Optional[str] = None
    result: Optional[float] = None


class BoundingBoxLabelAveragePrecisionResult(BaseModel):
    """
    Bounding Box Mean Average Precision Metric
    """
    labelName: Optional[str] = None
    averagePrecision: Optional[float] = None


class BoundingBoxLabelAveragePrecision(BaseModel):
    """
    Bounding Box Label Average Precision Metric
    """
    name: Optional[str] = None
    displayName: Optional[str] = None
    result: Optional[List[BoundingBoxLabelAveragePrecisionResult]] = None


class ConfusionMatrixAnnotationSpec(BaseModel):
    """
    Confusion Matrix Result
    """
    id: Optional[int] = None
    labelName: Optional[str] = None


class ConfusionMatrixRow(BaseModel):
    """
    Confusion Matrix Result
    """
    row: Optional[List[int]] = None


class ConfusionMatrixResult(BaseModel):
    """
    Confusion Matrix Result
    """
    annotationSpecs: Optional[List[ConfusionMatrixAnnotationSpec]] = None
    rows: Optional[List[ConfusionMatrixRow]] = None


class ConfusionMatrix(BaseModel):
    """
    Confusion Matrix
    """
    name: Optional[str] = None
    displayName: Optional[str] = None
    result: Optional[ConfusionMatrixResult] = None


class ObjectDetectionMetric(BaseModel):
    """
    Object Detection Metric
    """
    modelName: Optional[str] = None
    datasetName: Optional[str] = None
    baselineJobName: Optional[str] = None
    timestamp: Optional[str] = None
    labels: Optional[List[Label]] = None
    metrics: Optional[List[Union[
        BoundingBoxLabelMetric,
        BoundingBoxMeanAveragePrecision,
        BoundingBoxMeanAverageRecall,
        BoundingBoxLabelAveragePrecision,
        ConfusionMatrix]]] = None


LOSS_METRIC = "Loss"
MAP_METRIC = "mAP"
AP50_METRIC = "AP50"
AR_METRIC = "AR"


class Metric(BaseModel):
    name: Optional[str] = None
    result: Optional[float] = None


class TrainMetric(BaseModel):
    """
    Train Metric
    """
    epoch: Optional[int] = None
    step: Optional[int] = None
    metrics: Optional[List[Metric]] = None