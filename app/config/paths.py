import pathlib
from typing import Final

ROOT_DIR: Final[pathlib.Path] = pathlib.Path(__file__).parents[2]
LOGS_DIR: Final[pathlib.Path] = ROOT_DIR.joinpath("logs")
