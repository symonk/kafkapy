from typing import Protocol
from typing import runtime_checkable


@runtime_checkable
class Serializable(Protocol):
    """An interface for something that be serialized for json output."""

    def as_json(self) -> str:
        """Serialize the object and return the json representation of it."""
