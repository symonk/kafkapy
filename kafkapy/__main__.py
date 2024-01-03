from .constants import LibraryMeta
from .main import root_application

if __name__ == "__main__":
    raise SystemExit(root_application(prog_name=LibraryMeta.NAME))
