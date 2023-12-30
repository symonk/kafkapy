from typing import Protocol


class Serializable(Protocol):
    """An interface for something that be serialized for json output."""

    def as_json(self) -> str:
        """Serialize the object and return the json representation of it."""
