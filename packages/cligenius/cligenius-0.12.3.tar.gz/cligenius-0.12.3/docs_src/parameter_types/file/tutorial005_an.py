import cligenius
from typing_extensions import Annotated


def main(config: Annotated[cligenius.FileText, cligenius.Option(mode="a")]):
    config.write("This is a single line\n")
    print("Config line written")


if __name__ == "__main__":
    cligenius.run(main)
