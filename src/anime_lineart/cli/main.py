import argparse
import logging
from pathlib import Path

from anime_lineart.config import LineArtConfig
from anime_lineart.core.pipeline.pipeline import AnimeLineartPipeline


class AnimeLineartCLI:
    """Command line interface for anime-lineart."""

    def __init__(self, config: LineArtConfig | None = None) -> None:
        self.config = config or LineArtConfig()

    def run(self, argv: list[str] | None = None) -> int:
        """Run the CLI."""
        parser = argparse.ArgumentParser(
            prog="anime-lineart",
            description="Convert anime illustrations into editable SVG line art.",
        )
        parser.add_argument("input", help="Input image path: PNG, JPG, JPEG, or WEBP")
        args = parser.parse_args(argv)

        logging.basicConfig(level=logging.INFO, format="%(message)s")

        input_path = Path(args.input)
        if not input_path.exists():
            raise FileNotFoundError(f"Input file not found: {input_path}")

        if input_path.suffix.lower() not in self.config.supported_extensions:
            raise ValueError(f"Unsupported file format: {input_path.suffix}")

        output_path = input_path.with_name(f"{input_path.stem}_lineart.svg")

        logging.info("Loading image...")
        logging.info("Segmenting regions...")
        logging.info("Extracting contours...")
        logging.info("Exporting SVG...")

        pipeline = AnimeLineartPipeline(self.config)
        pipeline.run(input_path, output_path)

        print(f"✓ Created: {output_path}")
        return 0


def main() -> int:
    """Run anime-lineart."""
    return AnimeLineartCLI().run()
