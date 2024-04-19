import cligenius
from typing_extensions import Annotated


def main(name: Annotated[str, cligenius.Argument()]):
    print(f"Hello {name}")


if __name__ == "__main__":
    cligenius.run(main)
