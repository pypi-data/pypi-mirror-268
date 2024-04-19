import cligenius

import items
import users

app = cligenius.Cligenius()
app.add_cligenius(users.app, name="users")
app.add_cligenius(items.app, name="items")

if __name__ == "__main__":
    app()
