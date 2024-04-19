import cligenius

sub_app = cligenius.Cligenius()


@sub_app.command()
def hello():
    cligenius.echo("sub hello")


@sub_app.command()
def bye():
    cligenius.echo("sub bye")


cli = cligenius.Cligenius()
cli.add_cligenius(sub_app, name="sub")


@cli.command()
def top():
    cligenius.echo("top")
