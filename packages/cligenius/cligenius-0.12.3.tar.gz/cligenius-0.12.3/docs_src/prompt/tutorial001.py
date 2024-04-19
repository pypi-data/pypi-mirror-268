import cligenius


def main():
    person_name = cligenius.prompt("What's your name?")
    print(f"Hello {person_name}")


if __name__ == "__main__":
    cligenius.run(main)
