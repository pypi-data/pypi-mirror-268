from typing import Optional

import cligenius
from typing_extensions import Annotated


def name_callback(ctx: cligenius.Context, value: str):
    if ctx.resilient_parsing:
        return
    print("Validating name")
    if value != "Camila":
        raise cligenius.BadParameter("Only Camila is allowed")
    return value


def main(name: Annotated[Optional[str], cligenius.Option(callback=name_callback)] = None):
    print(f"Hello {name}")


if __name__ == "__main__":
    cligenius.run(main)
