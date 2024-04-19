import cligenius


def main(
    name: str = cligenius.Argument(
        "Wade Wilson", help="Who to greet", show_default="Deadpoolio the amazing's name"
    ),
):
    print(f"Hello {name}")


if __name__ == "__main__":
    cligenius.run(main)
