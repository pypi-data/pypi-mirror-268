import cligenius
import cligenius.main

cligenius.main.rich = None


def main(name: str = "morty"):
    print(name + 3)


if __name__ == "__main__":
    cligenius.run(main)
