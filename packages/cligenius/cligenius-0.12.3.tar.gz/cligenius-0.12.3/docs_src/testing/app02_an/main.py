import cligenius
from typing_extensions import Annotated

app = cligenius.Cligenius()


@app.command()
def main(name: str, email: Annotated[str, cligenius.Option(prompt=True)]):
    print(f"Hello {name}, your email is: {email}")


if __name__ == "__main__":
    app()
