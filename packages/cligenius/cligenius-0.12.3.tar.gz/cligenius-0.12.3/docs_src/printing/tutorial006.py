import cligenius


def main(name: str):
    cligenius.secho(f"Welcome here {name}", fg=cligenius.colors.MAGENTA)


if __name__ == "__main__":
    cligenius.run(main)
