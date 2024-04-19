import cligenius


def main(name: str = cligenius.Argument("World", metavar="✨username✨")):
    print(f"Hello {name}")


if __name__ == "__main__":
    cligenius.run(main)
