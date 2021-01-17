from os import PathLike
from typing import Union, Any

Filename = Union[str, bytes, PathLike[str], PathLike[bytes], int]
Mapping = dict[str, Any]
