from typing import List

import cligenius
from typing_extensions import Annotated


def main(number: Annotated[List[float], cligenius.Option()] = []):
    print(f"The sum is {sum(number)}")


if __name__ == "__main__":
    cligenius.run(main)
