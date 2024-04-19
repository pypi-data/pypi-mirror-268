import cligenius

app = cligenius.Cligenius()


@app.command()
def hello(name: str = "World", formal: bool = False):
    """
    Say hi
    """
    if formal:
        cligenius.echo(f"Good morning Ms. {name}")
    else:
        cligenius.echo(f"Hello {name}!")


@app.command()
def bye(friend: bool = False):
    """
    Say bye
    """
    if friend:
        cligenius.echo("Goodbye my friend")
    else:
        cligenius.echo("Goodbye")
