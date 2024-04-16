import collections.abc
import typing

from typing_extensions import TypeAlias  # Python 3.10+


StepTasksType: TypeAlias = tuple[int, ...]
StepTaskNumberType: TypeAlias = typing.Optional[StepTasksType]

#: A list of all valid option type literals
OptionTypeLiteral: TypeAlias = typing.Literal['string', 'boolean', 'integer', 'float']

#: A list of all deprecated option type literals
OptionDeprecatedTypeLiteral: TypeAlias = typing.Literal['str', 'bool', 'int']

#: A list of all valid option location literals
LocationLiteral: TypeAlias = typing.Literal['step', 'recipe', 'config', 'product']

#: Type alias for subdomain definition
SubDomainDefinitionType: TypeAlias = dict[
    LocationLiteral,
    typing.Union[str, collections.abc.Sequence[typing.Optional[str]], None]
]
