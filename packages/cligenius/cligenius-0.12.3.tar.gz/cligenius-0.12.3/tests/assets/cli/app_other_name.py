import cligenius

application = cligenius.Cligenius()


@application.command()
def callback(name: str = "World"):
    cligenius.echo(f"Hello {name}")
