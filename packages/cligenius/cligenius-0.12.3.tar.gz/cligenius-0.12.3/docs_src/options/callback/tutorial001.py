from typing import Optional

import cligenius


def name_callback(value: str):
    if value != "Camila":
        raise cligenius.BadParameter("Only Camila is allowed")
    return value


def main(name: Optional[str] = cligenius.Option(default=None, callback=name_callback)):
    print(f"Hello {name}")


if __name__ == "__main__":
    cligenius.run(main)
