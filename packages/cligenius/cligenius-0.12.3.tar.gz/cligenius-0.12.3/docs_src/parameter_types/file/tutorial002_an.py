import cligenius
from typing_extensions import Annotated


def main(config: Annotated[cligenius.FileTextWrite, cligenius.Option()]):
    config.write("Some config written by the app")
    print("Config written")


if __name__ == "__main__":
    cligenius.run(main)
