import cligenius


def main(name: str = cligenius.Argument()):
    print(f"Hello {name}")


if __name__ == "__main__":
    cligenius.run(main)
