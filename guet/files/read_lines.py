from typing import List, Union
from pathlib import Path


def read_lines(path: Union[Path, str]) -> List[str]:
    if type(path) is str:
        return _read_lines_from_path(Path(path))
    else:
        return _read_lines_from_path(path)


def _read_lines_from_path(path: Path) -> List[str]:
    all_lines = path.read_text().split('\n')
    if all_lines[len(all_lines) - 1] == '':
        del all_lines[len(all_lines) - 1]
    return all_lines
