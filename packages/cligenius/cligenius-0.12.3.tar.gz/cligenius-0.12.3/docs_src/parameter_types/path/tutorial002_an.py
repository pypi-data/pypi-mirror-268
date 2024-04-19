from pathlib import Path

import cligenius
from typing_extensions import Annotated


def main(
    config: Annotated[
        Path,
        cligenius.Option(
            exists=True,
            file_okay=True,
            dir_okay=False,
            writable=False,
            readable=True,
            resolve_path=True,
        ),
    ],
):
    text = config.read_text()
    print(f"Config file contents: {text}")


if __name__ == "__main__":
    cligenius.run(main)
