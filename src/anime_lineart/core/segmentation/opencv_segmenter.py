from typing import cast

import cv2
import numpy as np
import numpy.typing as npt

from anime_lineart.config import LineArtConfig
from anime_lineart.core.segmentation.base import BaseSegmenter


class OpenCVSegmenter(BaseSegmenter):
    """Simple OpenCV-based color simplifier."""

    def __init__(self, config: LineArtConfig) -> None:
        self.config = config

    def segment(self, image: npt.NDArray[np.uint8]) -> npt.NDArray[np.uint8]:
        """Reduce small color variations while preserving major anime regions."""
        blurred = cv2.bilateralFilter(image, d=9, sigmaColor=75, sigmaSpace=75)
        data = blurred.reshape((-1, 3)).astype(np.float32)

        criteria = (
            cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER,
            20,
            1.0,
        )
        _compactness, labels, centers = cv2.kmeans(
            data,
            self.config.color_clusters,
            np.empty((0, 1), dtype=np.int32),
            criteria,
            3,
            cv2.KMEANS_PP_CENTERS,
        )

        labels_array = cast(npt.NDArray[np.int32], labels)
        centers_array = cast(npt.NDArray[np.float32], centers)

        centers_uint8 = centers_array.astype(np.uint8)
        quantized = centers_uint8[labels_array.flatten()].reshape(image.shape)
        return cast(npt.NDArray[np.uint8], quantized.astype(np.uint8))
