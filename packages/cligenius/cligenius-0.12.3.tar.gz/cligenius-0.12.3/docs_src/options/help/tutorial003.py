import cligenius


def main(fullname: str = cligenius.Option("Wade Wilson", show_default=False)):
    print(f"Hello {fullname}")


if __name__ == "__main__":
    cligenius.run(main)
