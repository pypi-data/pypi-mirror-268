import cligenius


def main(
    id: int = cligenius.Argument(..., min=0, max=1000),
    rank: int = cligenius.Option(0, max=10, clamp=True),
    score: float = cligenius.Option(0, min=0, max=100, clamp=True),
):
    print(f"ID is {id}")
    print(f"--rank is {rank}")
    print(f"--score is {score}")


if __name__ == "__main__":
    cligenius.run(main)
