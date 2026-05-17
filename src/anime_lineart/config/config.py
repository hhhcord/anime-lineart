from dataclasses import dataclass


@dataclass(frozen=True)
class LineArtConfig:
    """Configuration for anime line art extraction."""

    stroke_width: float = 1.0
    min_contour_length: float = 24.0
    smoothing_epsilon_ratio: float = 0.002
    color_clusters: int = 24
    morph_kernel_size: int = 3
    supported_extensions: tuple[str, ...] = (".png", ".jpg", ".jpeg", ".webp")
