import cligenius


def main(force: bool = cligenius.Option(False, "--force/--no-force", "-f/-F")):
    if force:
        print("Forcing operation")
    else:
        print("Not forcing")


if __name__ == "__main__":
    cligenius.run(main)
