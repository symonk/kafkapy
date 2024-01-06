import typing

from pydantic import BaseModel

BootstrapServersTypes = typing.Optional[typing.Sequence[str]]
BootstrapServersSplitTypes = typing.Tuple[typing.Tuple[str, int], ...]
StringDictTypes = typing.Dict[str, str]


SerializableInstanceType = typing.Union[BaseModel, str]
