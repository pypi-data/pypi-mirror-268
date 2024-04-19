import cligenius


def main(user_name: str = cligenius.Option(..., "-n")):
    print(f"Hello {user_name}")


if __name__ == "__main__":
    cligenius.run(main)
