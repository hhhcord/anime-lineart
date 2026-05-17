from pathlib import Path

from anime_lineart.config import LineArtConfig
from anime_lineart.core.contour.opencv_contour_extractor import OpenCVContourExtractor
from anime_lineart.core.optimization.opencv_path_optimizer import OpenCVPathOptimizer
from anime_lineart.core.segmentation.opencv_segmenter import OpenCVSegmenter
from anime_lineart.exporters.svg_exporter import SVGExporter
from anime_lineart.utils.image_loader import ImageLoader


class AnimeLineartPipeline:
    """Full image-to-SVG line art pipeline."""

    def __init__(self, config: LineArtConfig) -> None:
        self.config = config
        self.loader = ImageLoader()
        self.segmenter = OpenCVSegmenter(config)
        self.contour_extractor = OpenCVContourExtractor(config)
        self.path_optimizer = OpenCVPathOptimizer(config)
        self.svg_exporter = SVGExporter(config)

    def run(self, input_path: Path, output_path: Path) -> None:
        """Convert an input image to SVG line art."""
        image = self.loader.load(input_path)
        height, width = image.shape[:2]

        segmented = self.segmenter.segment(image)
        contours = self.contour_extractor.extract(segmented)
        paths = self.path_optimizer.optimize(contours)

        self.svg_exporter.export(paths, output_path, width=width, height=height)
