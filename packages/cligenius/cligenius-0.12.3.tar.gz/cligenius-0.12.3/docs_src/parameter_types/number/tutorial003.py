import cligenius


def main(verbose: int = cligenius.Option(0, "--verbose", "-v", count=True)):
    print(f"Verbose level is {verbose}")


if __name__ == "__main__":
    cligenius.run(main)
