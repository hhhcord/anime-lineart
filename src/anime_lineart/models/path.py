from dataclasses import dataclass


@dataclass(frozen=True)
class SvgPath:
    """A single SVG stroke path."""

    d: str
