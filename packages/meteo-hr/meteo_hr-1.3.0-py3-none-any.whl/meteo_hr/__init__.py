from typing import NamedTuple, Union
from importlib import metadata

try:
    __version__ = metadata.version("meteo_hr")
except metadata.PackageNotFoundError:
    __version__ = "0.0.0"


class Place3D(NamedTuple):
    name: str
    slug: str
    region: str


class Place7D(NamedTuple):
    name: str
    code: str


Place = Union[Place3D, Place7D]
