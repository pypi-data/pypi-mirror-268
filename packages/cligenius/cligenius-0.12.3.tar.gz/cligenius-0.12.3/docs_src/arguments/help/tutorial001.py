import cligenius


def main(name: str = cligenius.Argument(..., help="The name of the user to greet")):
    print(f"Hello {name}")


if __name__ == "__main__":
    cligenius.run(main)
