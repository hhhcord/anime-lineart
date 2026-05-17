from abc import ABC, abstractmethod

import numpy as np
import numpy.typing as npt


class BaseContourExtractor(ABC):
    """Base class for contour extraction."""

    @abstractmethod
    def extract(self, image: npt.NDArray[np.uint8]) -> list[npt.NDArray[np.int32]]:
        """Extract contours from an image."""
