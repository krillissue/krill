import logging
from pathlib import Path
import click
from .log import setup_logger
from .frontend import Library, Executable, Warning

__all__ = ["Library", "Executable", "Warning"]
setup_logger()

@click.command()
@click.option("--source", type=Path, default=Path.cwd(), help="Path to root krillfile.py")
def main(source: Path):
    if source.is_dir():
        source /= "krillfile.py"

    if not source.exists():
        logging.error("Could not find `krillfile.py` at %s", source)
        return 1

    return 0
