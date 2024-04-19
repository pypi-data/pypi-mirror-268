import cligenius


def complete_name():
    return ["Camila", "Carlos", "Sebastian"]


app = cligenius.Cligenius()


@app.command()
def main(
    name: str = cligenius.Option(
        "World", help="The name to say hi to.", autocompletion=complete_name
    ),
):
    print(f"Hello {name}")


if __name__ == "__main__":
    app()
