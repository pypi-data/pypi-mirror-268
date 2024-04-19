import cligenius

app = cligenius.Cligenius()


@app.command()
def main(name: str):
    print(f"Hello {name}")


if __name__ == "__main__":
    app()
