import random

import cligenius


def get_name():
    return random.choice(["Deadpool", "Rick", "Morty", "Hiro"])


def main(name: str = cligenius.Argument(default_factory=get_name)):
    print(f"Hello {name}")


if __name__ == "__main__":
    cligenius.run(main)
