import cligenius


def main(
    name: str = cligenius.Option(..., "--name", "-n"),
    formal: bool = cligenius.Option(False, "--formal", "-f"),
):
    if formal:
        print(f"Good day Ms. {name}.")
    else:
        print(f"Hello {name}")


if __name__ == "__main__":
    cligenius.run(main)
