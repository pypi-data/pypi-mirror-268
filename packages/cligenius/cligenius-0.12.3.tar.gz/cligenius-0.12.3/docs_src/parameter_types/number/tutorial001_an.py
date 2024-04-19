import cligenius
from typing_extensions import Annotated


def main(
    id: Annotated[int, cligenius.Argument(min=0, max=1000)],
    age: Annotated[int, cligenius.Option(min=18)] = 20,
    score: Annotated[float, cligenius.Option(max=100)] = 0,
):
    print(f"ID is {id}")
    print(f"--age is {age}")
    print(f"--score is {score}")


if __name__ == "__main__":
    cligenius.run(main)
