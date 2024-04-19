import cligenius


def main(
    name: str = cligenius.Argument(..., help="Who to greet"),
    lastname: str = cligenius.Argument(
        "", help="The last name", rich_help_panel="Secondary Arguments"
    ),
    age: str = cligenius.Argument(
        "", help="The user's age", rich_help_panel="Secondary Arguments"
    ),
):
    """
    Say hi to NAME very gently, like Dirk.
    """
    print(f"Hello {name}")


if __name__ == "__main__":
    cligenius.run(main)
