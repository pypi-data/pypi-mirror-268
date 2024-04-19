import cligenius

app = cligenius.Cligenius()


def users_callback():
    print("Running a users command")


users_app = cligenius.Cligenius(callback=users_callback)
app.add_cligenius(users_app, name="users")


@users_app.command()
def create(name: str):
    print(f"Creating user: {name}")


if __name__ == "__main__":
    app()
