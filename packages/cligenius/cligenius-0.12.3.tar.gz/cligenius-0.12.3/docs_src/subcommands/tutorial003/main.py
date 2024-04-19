import cligenius

import items
import lands
import users

app = cligenius.Cligenius()
app.add_cligenius(users.app, name="users")
app.add_cligenius(items.app, name="items")
app.add_cligenius(lands.app, name="lands")

if __name__ == "__main__":
    app()
