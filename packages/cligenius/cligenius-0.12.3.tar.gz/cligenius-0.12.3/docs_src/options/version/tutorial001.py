from typing import Optional

import cligenius

__version__ = "0.1.0"


def version_callback(value: bool):
    if value:
        print(f"Awesome CLI Version: {__version__}")
        raise cligenius.Exit()


def main(
    name: str = cligenius.Option("World"),
    version: Optional[bool] = cligenius.Option(
        None, "--version", callback=version_callback
    ),
):
    print(f"Hello {name}")


if __name__ == "__main__":
    cligenius.run(main)
