from typing import cast

import cv2
import numpy as np
import numpy.typing as npt

from anime_lineart.config import LineArtConfig
from anime_lineart.core.contour.base import BaseContourExtractor


class OpenCVContourExtractor(BaseContourExtractor):
    """Extract contours from simplified color regions."""

    def __init__(self, config: LineArtConfig) -> None:
        self.config = config

    def extract(self, image: npt.NDArray[np.uint8]) -> list[npt.NDArray[np.int32]]:
        """Extract connected contours from region boundaries."""
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, threshold1=40, threshold2=120)

        kernel = np.ones(
            (self.config.morph_kernel_size, self.config.morph_kernel_size),
            dtype=np.uint8,
        )
        edges = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)

        contours, _hierarchy = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

        result: list[npt.NDArray[np.int32]] = []
        for contour in contours:
            contour_array = cast(npt.NDArray[np.int32], contour)
            if cv2.arcLength(contour_array, closed=False) >= self.config.min_contour_length:
                result.append(contour_array)

        return result
