import cligenius

app = cligenius.Cligenius()


def users():
    """
    Manage users in the app.
    """


users_app = cligenius.Cligenius(callback=users)
app.add_cligenius(users_app)


@users_app.command()
def create(name: str):
    print(f"Creating user: {name}")


if __name__ == "__main__":
    app()
