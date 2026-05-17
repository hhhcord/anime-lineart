from abc import ABC, abstractmethod

import numpy as np
import numpy.typing as npt


class BaseSegmenter(ABC):
    """Base class for image segmentation."""

    @abstractmethod
    def segment(self, image: npt.NDArray[np.uint8]) -> npt.NDArray[np.uint8]:
        """Return a simplified image for edge extraction."""
