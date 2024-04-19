from typing import Union

import cligenius

app = cligenius.Cligenius(rich_markup_mode="rich")


@app.command()
def create(
    username: str = cligenius.Argument(..., help="The username to create"),
    lastname: str = cligenius.Argument(
        "", help="The last name of the new user", rich_help_panel="Secondary Arguments"
    ),
    force: bool = cligenius.Option(False, help="Force the creation of the user"),
    age: Union[int, None] = cligenius.Option(
        None, help="The age of the new user", rich_help_panel="Additional Data"
    ),
    favorite_color: Union[str, None] = cligenius.Option(
        None,
        help="The favorite color of the new user",
        rich_help_panel="Additional Data",
    ),
):
    """
    [green]Create[/green] a new user. :sparkles:
    """
    print(f"Creating user: {username}")


@app.command(rich_help_panel="Utils and Configs")
def config(configuration: str):
    """
    [blue]Configure[/blue] the system. :wrench:
    """
    print(f"Configuring the system with: {configuration}")


if __name__ == "__main__":
    app()
