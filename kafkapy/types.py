import typing

from pydantic import BaseModel

BootstrapServersTypes = typing.Optional[typing.Sequence[str]]
StringDictTypes = typing.Dict[str, str]


SerializableInstanceType = typing.Union[BaseModel, str]
