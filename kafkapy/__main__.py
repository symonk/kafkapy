from .main import root_application
from .constants import LibraryMeta

if __name__ == "__main__":
    raise SystemExit(root_application(prog_name=LibraryMeta.NAME))
