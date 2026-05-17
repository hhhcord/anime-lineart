from pathlib import Path

from anime_lineart.cli.main import AnimeLineartCLI


def test_cli_creates_svg() -> None:
    """CLI should generate an SVG file."""
    input_path = Path("examples/test.png")

    cli = AnimeLineartCLI()
    result = cli.run([str(input_path)])

    output_path = Path("examples/test_lineart.svg")

    assert result == 0
    assert output_path.exists()
