import pkg_resources
from .constants import LibraryMeta

__version__ = pkg_resources.get_distribution(LibraryMeta.NAME)
