import click
import cligenius


@click.group()
def cli():
    pass


@cli.command()
def initdb():
    click.echo("Initialized the database")


@cli.command()
def dropdb():
    click.echo("Dropped the database")


app = cligenius.Cligenius()


@app.command()
def sub():
    """
    A single-command Cligenius sub app
    """
    print("Cligenius is now below Click, the Click app is the top level")


cligenius_click_object = cligenius.main.get_command(app)

cli.add_command(cligenius_click_object, "sub")

if __name__ == "__main__":
    cli()
