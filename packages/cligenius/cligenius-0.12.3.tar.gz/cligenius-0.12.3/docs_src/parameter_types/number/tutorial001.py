import cligenius


def main(
    id: int = cligenius.Argument(..., min=0, max=1000),
    age: int = cligenius.Option(20, min=18),
    score: float = cligenius.Option(0, max=100),
):
    print(f"ID is {id}")
    print(f"--age is {age}")
    print(f"--score is {score}")


if __name__ == "__main__":
    cligenius.run(main)
