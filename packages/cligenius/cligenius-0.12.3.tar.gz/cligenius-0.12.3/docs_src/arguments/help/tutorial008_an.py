import cligenius
from typing_extensions import Annotated


def main(name: Annotated[str, cligenius.Argument(hidden=True)] = "World"):
    """
    Say hi to NAME very gently, like Dirk.
    """
    print(f"Hello {name}")


if __name__ == "__main__":
    cligenius.run(main)
