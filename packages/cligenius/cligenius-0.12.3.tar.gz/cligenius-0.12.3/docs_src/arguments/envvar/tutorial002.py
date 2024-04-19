import cligenius


def main(name: str = cligenius.Argument("World", envvar=["AWESOME_NAME", "GOD_NAME"])):
    print(f"Hello Mr. {name}")


if __name__ == "__main__":
    cligenius.run(main)
