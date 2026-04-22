from pathlib import Path
from typing import Tuple, Union


def collection_key(item) -> Tuple[bool, Union[int, str], str]:
    path = Path(str(item.path))
    stem = path.stem

    if stem.isdigit():
        return (False, int(stem), item.nodeid)

    return (True, stem, item.nodeid)


def pytest_collection_modifyitems(items) -> None:
    items.sort(key=collection_key)
