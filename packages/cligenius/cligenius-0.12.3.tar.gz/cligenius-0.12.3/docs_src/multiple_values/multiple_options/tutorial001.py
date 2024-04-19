from typing import List, Optional

import cligenius


def main(user: Optional[List[str]] = cligenius.Option(None)):
    if not user:
        print(f"No provided users (raw input = {user})")
        raise cligenius.Abort()
    for u in user:
        print(f"Processing user: {u}")


if __name__ == "__main__":
    cligenius.run(main)
