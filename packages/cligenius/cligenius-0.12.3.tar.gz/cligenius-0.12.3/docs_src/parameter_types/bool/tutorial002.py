from typing import Optional

import cligenius


def main(accept: Optional[bool] = cligenius.Option(None, "--accept/--reject")):
    if accept is None:
        print("I don't know what you want yet")
    elif accept:
        print("Accepting!")
    else:
        print("Rejecting!")


if __name__ == "__main__":
    cligenius.run(main)
