import cligenius

app = cligenius.Cligenius()


@app.command()
def main(name: str, email: str = cligenius.Option(..., prompt=True)):
    print(f"Hello {name}, your email is: {email}")


if __name__ == "__main__":
    app()
