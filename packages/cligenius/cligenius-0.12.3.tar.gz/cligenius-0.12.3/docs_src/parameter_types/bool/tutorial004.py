import cligenius


def main(in_prod: bool = cligenius.Option(True, " /--demo", " /-d")):
    if in_prod:
        print("Running in production")
    else:
        print("Running demo")


if __name__ == "__main__":
    cligenius.run(main)
