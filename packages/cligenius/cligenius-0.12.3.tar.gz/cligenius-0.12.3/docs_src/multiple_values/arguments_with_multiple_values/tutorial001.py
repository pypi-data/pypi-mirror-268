from pathlib import Path
from typing import List

import cligenius


def main(files: List[Path], celebration: str):
    for path in files:
        if path.is_file():
            print(f"This file exists: {path.name}")
            print(celebration)


if __name__ == "__main__":
    cligenius.run(main)
