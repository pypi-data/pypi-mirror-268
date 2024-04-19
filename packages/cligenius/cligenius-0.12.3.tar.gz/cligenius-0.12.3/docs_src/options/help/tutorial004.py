import cligenius


def main(
    fullname: str = cligenius.Option(
        "Wade Wilson", show_default="Deadpoolio the amazing's name"
    ),
):
    print(f"Hello {fullname}")


if __name__ == "__main__":
    cligenius.run(main)
