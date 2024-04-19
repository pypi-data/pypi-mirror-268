import cligenius

app = cligenius.Cligenius()

users_app = cligenius.Cligenius()
app.add_cligenius(users_app, name="users")


@users_app.callback()
def users_callback():
    print("Running a users command")


@users_app.command()
def create(name: str):
    print(f"Creating user: {name}")


if __name__ == "__main__":
    app()
