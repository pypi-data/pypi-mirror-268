import cligenius


def main(name: str = cligenius.Argument("Wade Wilson")):
    print(f"Hello {name}")


if __name__ == "__main__":
    cligenius.run(main)
