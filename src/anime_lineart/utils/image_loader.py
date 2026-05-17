from pathlib import Path
from typing import cast

import cv2
import numpy as np
import numpy.typing as npt


class ImageLoader:
    """Load image files with OpenCV."""

    def load(self, path: Path) -> npt.NDArray[np.uint8]:
        """Load an image as BGR uint8 array."""
        image = cv2.imread(str(path), cv2.IMREAD_COLOR)
        if image is None:
            raise ValueError(f"Failed to load image: {path}")
        return cast(npt.NDArray[np.uint8], image.astype(np.uint8))
