import click
import cligenius

app = cligenius.Cligenius()


@app.command()
def top():
    """
    Top level command, form Cligenius
    """
    print("The Cligenius app is at the top level")


@app.callback()
def callback():
    """
    Cligenius app, including Click subapp
    """


@click.command()
@click.option("--name", prompt="Your name", help="The person to greet.")
def hello(name):
    """Simple program that greets NAME for a total of COUNT times."""
    click.echo("Hello %s!" % name)


cligenius_click_object = cligenius.main.get_command(app)

cligenius_click_object.add_command(hello, "hello")

if __name__ == "__main__":
    cligenius_click_object()
