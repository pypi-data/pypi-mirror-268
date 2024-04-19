import cligenius


def main(
    name: str,
    password: str = cligenius.Option(
        ..., prompt=True, confirmation_prompt=True, hide_input=True
    ),
):
    print(f"Hello {name}. Doing something very secure with password.")
    print(f"...just kidding, here it is, very insecure: {password}")


if __name__ == "__main__":
    cligenius.run(main)
