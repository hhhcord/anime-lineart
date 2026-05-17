from abc import ABC, abstractmethod

import numpy as np
import numpy.typing as npt

from anime_lineart.models.path import SvgPath


class BasePathOptimizer(ABC):
    """Base class for converting contours to optimized SVG paths."""

    @abstractmethod
    def optimize(self, contours: list[npt.NDArray[np.int32]]) -> list[SvgPath]:
        """Convert contours to SVG paths."""
