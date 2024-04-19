import cligenius


def main(name: str = cligenius.Argument("World", hidden=True)):
    """
    Say hi to NAME very gently, like Dirk.
    """
    print(f"Hello {name}")


if __name__ == "__main__":
    cligenius.run(main)
