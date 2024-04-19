from typing import List

import cligenius


def main(number: List[float] = cligenius.Option([])):
    print(f"The sum is {sum(number)}")


if __name__ == "__main__":
    cligenius.run(main)
