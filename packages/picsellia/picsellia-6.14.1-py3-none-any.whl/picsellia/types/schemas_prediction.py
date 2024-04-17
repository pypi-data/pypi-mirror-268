from typing import List

from pydantic import BaseModel, root_validator

from picsellia.types.enums import InferenceType


class PredictionFormat(BaseModel):
    @property
    def model_type(cls) -> InferenceType:
        raise Exception()


class ClassificationPredictionFormat(PredictionFormat):
    detection_classes: List[int]
    detection_scores: List[float]

    @property
    def model_type(cls) -> InferenceType:
        return InferenceType.CLASSIFICATION


class DetectionPredictionFormat(PredictionFormat):
    detection_classes: List[int]
    detection_boxes: List[List[int]]
    detection_scores: List[float]

    @property
    def model_type(cls) -> InferenceType:
        return InferenceType.OBJECT_DETECTION

    @root_validator
    def check_sizes(cls, values):
        labels, scores, boxes = (
            values.get("detection_classes"),
            values.get("detection_scores"),
            values.get("detection_boxes"),
        )

        if (
            labels is None
            or scores is None
            or boxes is None is None
            or len(labels) != len(scores)
            or len(boxes) != len(labels)
        ):
            raise ValueError("incoherent lists")

        return values


class SegmentationPredictionFormat(PredictionFormat):
    detection_classes: List[int]
    detection_boxes: List[List[int]]
    detection_scores: List[float]
    detection_masks: List[List[List[int]]]

    @property
    def model_type(cls) -> InferenceType:
        return InferenceType.SEGMENTATION

    @root_validator
    def check_sizes(cls, values):
        labels, boxes, scores, masks = (
            values.get("detection_classes"),
            values.get("detection_boxes"),
            values.get("detection_scores"),
            values.get("detection_masks"),
        )

        if (
            labels is None
            or scores is None
            or boxes is None
            or masks is None
            or len(labels) != len(scores)
            or len(boxes) != len(labels)
            or len(masks) != len(labels)
        ):
            raise ValueError("incoherent lists")

        return values
