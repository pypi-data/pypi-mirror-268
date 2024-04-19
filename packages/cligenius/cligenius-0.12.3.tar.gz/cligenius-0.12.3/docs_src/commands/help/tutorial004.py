import cligenius

app = cligenius.Cligenius(rich_markup_mode="rich")


@app.command()
def create(
    username: str = cligenius.Argument(
        ..., help="The username to be [green]created[/green]"
    ),
):
    """
    [bold green]Create[/bold green] a new [italic]shiny[/italic] user. :sparkles:

    This requires a [underline]username[/underline].
    """
    print(f"Creating user: {username}")


@app.command(help="[bold red]Delete[/bold red] a user with [italic]USERNAME[/italic].")
def delete(
    username: str = cligenius.Argument(..., help="The username to be [red]deleted[/red]"),
    force: bool = cligenius.Option(
        False, help="Force the [bold red]deletion[/bold red] :boom:"
    ),
):
    """
    Some internal utility function to delete.
    """
    print(f"Deleting user: {username}")


if __name__ == "__main__":
    app()
