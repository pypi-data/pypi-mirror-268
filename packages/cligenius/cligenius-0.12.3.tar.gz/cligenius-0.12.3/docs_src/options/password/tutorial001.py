import cligenius


def main(
    name: str, email: str = cligenius.Option(..., prompt=True, confirmation_prompt=True)
):
    print(f"Hello {name}, your email is {email}")


if __name__ == "__main__":
    cligenius.run(main)
