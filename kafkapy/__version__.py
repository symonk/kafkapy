from importlib import metadata

from .constants import LibraryMeta

__version__ = metadata.version(LibraryMeta.NAME)
