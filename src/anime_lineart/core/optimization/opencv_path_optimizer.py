from typing import cast

import cv2
import numpy as np
import numpy.typing as npt

from anime_lineart.config import LineArtConfig
from anime_lineart.core.optimization.base import BasePathOptimizer
from anime_lineart.models.path import SvgPath


class OpenCVPathOptimizer(BasePathOptimizer):
    """Simplify OpenCV contours into SVG path strings."""

    def __init__(self, config: LineArtConfig) -> None:
        self.config = config

    def optimize(self, contours: list[npt.NDArray[np.int32]]) -> list[SvgPath]:
        """Convert contours to lightly smoothed continuous SVG paths."""
        paths: list[SvgPath] = []

        for contour in contours:
            epsilon = self.config.smoothing_epsilon_ratio * cv2.arcLength(contour, closed=False)
            approx = cv2.approxPolyDP(contour, epsilon, closed=False)
            points = cast(npt.NDArray[np.int32], approx.reshape(-1, 2))

            if len(points) < 2:
                continue

            path_data = self._to_svg_path(points)
            paths.append(SvgPath(d=path_data))

        return paths

    def _to_svg_path(self, points: npt.NDArray[np.int32]) -> str:
        first_x, first_y = points[0]
        commands = [f"M {int(first_x)} {int(first_y)}"]

        for x, y in points[1:]:
            commands.append(f"L {int(x)} {int(y)}")

        return " ".join(commands)
