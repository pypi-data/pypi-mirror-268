from typing import Optional

import cligenius
from typing_extensions import Annotated

__version__ = "0.1.0"


def version_callback(value: bool):
    if value:
        print(f"Awesome CLI Version: {__version__}")
        raise cligenius.Exit()


def name_callback(name: str):
    if name != "Camila":
        raise cligenius.BadParameter("Only Camila is allowed")


def main(
    name: Annotated[str, cligenius.Option(callback=name_callback)],
    version: Annotated[
        Optional[bool], cligenius.Option("--version", callback=version_callback)
    ] = None,
):
    print(f"Hello {name}")


if __name__ == "__main__":
    cligenius.run(main)
