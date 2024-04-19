import cligenius
from typing_extensions import Annotated


def main(
    name: Annotated[str, cligenius.Option("--name", "-n")],
    formal: Annotated[bool, cligenius.Option("--formal", "-f")] = False,
):
    if formal:
        print(f"Good day Ms. {name}.")
    else:
        print(f"Hello {name}")


if __name__ == "__main__":
    cligenius.run(main)
