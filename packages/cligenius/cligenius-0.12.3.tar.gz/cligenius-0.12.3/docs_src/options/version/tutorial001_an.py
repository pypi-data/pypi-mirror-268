from typing import Optional

import cligenius
from typing_extensions import Annotated

__version__ = "0.1.0"


def version_callback(value: bool):
    if value:
        print(f"Awesome CLI Version: {__version__}")
        raise cligenius.Exit()


def main(
    name: Annotated[str, cligenius.Option()] = "World",
    version: Annotated[
        Optional[bool], cligenius.Option("--version", callback=version_callback)
    ] = None,
):
    print(f"Hello {name}")


if __name__ == "__main__":
    cligenius.run(main)
