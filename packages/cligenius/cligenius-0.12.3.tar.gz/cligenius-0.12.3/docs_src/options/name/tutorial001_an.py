import cligenius
from typing_extensions import Annotated


def main(user_name: Annotated[str, cligenius.Option("--name")]):
    print(f"Hello {user_name}")


if __name__ == "__main__":
    cligenius.run(main)
