import cligenius

sub_app = cligenius.Cligenius()

variable = "Some text"


@sub_app.command()
def hello(name: str = "World", age: int = cligenius.Option(0, help="The age of the user")):
    """
    Say Hello
    """
    cligenius.echo(f"Hello {name}")


@sub_app.command()
def hi(user: str = cligenius.Argument("World", help="The name of the user to greet")):
    """
    Say Hi
    """


@sub_app.command()
def bye():
    """
    Say bye
    """
    cligenius.echo("sub bye")


app = cligenius.Cligenius(help="Demo App", epilog="The end")
app.add_cligenius(sub_app, name="sub")


@app.command()
def top():
    """
    Top command
    """
    cligenius.echo("top")
