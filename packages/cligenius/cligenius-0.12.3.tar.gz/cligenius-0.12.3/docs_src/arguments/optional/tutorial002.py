from typing import Optional

import cligenius


def main(name: Optional[str] = cligenius.Argument(default=None)):
    if name is None:
        print("Hello World!")
    else:
        print(f"Hello {name}")


if __name__ == "__main__":
    cligenius.run(main)
