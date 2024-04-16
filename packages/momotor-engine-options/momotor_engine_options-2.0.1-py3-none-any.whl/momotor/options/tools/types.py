import collections.abc
import typing
from os import PathLike

from typing_extensions import TypeAlias  # Python 3.10+

from .tool import ToolName

PathList: TypeAlias = typing.Optional[collections.abc.Iterable[typing.Union[str, PathLike]]]
PathTuple: TypeAlias = typing.Optional[tuple[typing.Union[str, PathLike], ...]]
StrPathOrToolName: TypeAlias = typing.Union[str, PathLike, ToolName]
ToolSet: TypeAlias = frozenset[StrPathOrToolName]
ToolRequirements: TypeAlias = collections.abc.Mapping[str, ToolSet]
