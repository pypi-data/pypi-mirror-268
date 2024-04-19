from typing import Optional

import cligenius
from typing_extensions import Annotated


def main(name: Annotated[Optional[str], cligenius.Argument()] = None):
    if name is None:
        print("Hello World!")
    else:
        print(f"Hello {name}")


if __name__ == "__main__":
    cligenius.run(main)
