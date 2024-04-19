import cligenius
from typing_extensions import Annotated

app = cligenius.Cligenius()


@app.command()
def main(name: Annotated[str, cligenius.Option(help="The name to say hi to.")] = "World"):
    print(f"Hello {name}")


if __name__ == "__main__":
    app()
