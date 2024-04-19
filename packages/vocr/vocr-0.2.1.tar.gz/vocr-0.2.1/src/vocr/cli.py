__all__ = ["cli"]

import platform
from pathlib import Path

import click

from vocr import __title__, __version__
from vocr.vocr import VietOCR


@click.command(name="version")
def version() -> None:
    """Show current version"""
    ver_msg = f"{__title__} v{__version__}"
    click.echo(
        f"{ver_msg}\n"
        f"- os/type: {platform.system().lower()}\n"
        f"- os/kernel: {platform.version()}\n"
        f"- os/arch: {platform.machine().lower()}\n"
        f"- python version: {platform.python_version()}\n"
    )


@click.command(name="ocr")
@click.argument("src", type=str)
@click.option(
    "--preprocess",
    "-p",
    "preprocess",
    type=click.Choice(["thresh", "blur"]),
    default="thresh",
    show_default=True,
    help="Preprocess image",
)
@click.option(
    "--output",
    "-o",
    "output",
    type=str,
    default=None,
    show_default=True,
    help="Output location",
)
def ocr(src: str, preprocess: str, output: str) -> None:
    """Performs OCR on file/directory"""
    instance = VietOCR(Path(src))
    instance.ocr(save_destination=output, preprocess=preprocess)  # type: ignore


@click.group(name="cli")
def cli() -> None:
    """vocr's command line interface"""
    pass


cli.add_command(version)
cli.add_command(ocr)
