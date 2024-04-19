import cligenius

app = cligenius.Cligenius()


@app.command()
def main(name: str = "morty"):
    print(name)


broken_app = cligenius.Cligenius()


@broken_app.command()
def broken(name: str = "morty"):
    print(name + 3)


if __name__ == "__main__":
    app(standalone_mode=False)

    cligenius.main.get_command(broken_app)()
