from pathlib import Path

import svgwrite

from anime_lineart.config import LineArtConfig
from anime_lineart.models.path import SvgPath


class SVGExporter:
    """Export SVG stroke paths."""

    def __init__(self, config: LineArtConfig) -> None:
        self.config = config

    def export(self, paths: list[SvgPath], output_path: Path, width: int, height: int) -> None:
        """Write paths to a transparent-background SVG file."""
        drawing = svgwrite.Drawing(
            str(output_path),
            size=(f"{width}px", f"{height}px"),
            viewBox=f"0 0 {width} {height}",
        )

        for path in paths:
            drawing.add(
                drawing.path(
                    d=path.d,
                    fill="none",
                    stroke="black",
                    stroke_width=self.config.stroke_width,
                    stroke_linecap="round",
                    stroke_linejoin="round",
                )
            )

        drawing.save()
