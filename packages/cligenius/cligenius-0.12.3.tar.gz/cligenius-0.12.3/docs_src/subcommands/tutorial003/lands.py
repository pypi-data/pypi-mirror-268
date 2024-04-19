import cligenius

import reigns
import towns

app = cligenius.Cligenius()
app.add_cligenius(reigns.app, name="reigns")
app.add_cligenius(towns.app, name="towns")

if __name__ == "__main__":
    app()
