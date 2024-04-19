import cligenius
from typing_extensions import Annotated


def main(
    project_name: Annotated[str, cligenius.Option(prompt=True, confirmation_prompt=True)],
):
    print(f"Deleting project {project_name}")


if __name__ == "__main__":
    cligenius.run(main)
