import random

import typer


def get_name():
    return random.choice(["Deadpool", "Rick", "Morty", "Hiro"])


def main(name: str = typer.Argument(get_name)):
    print(f"Hello {name}")


if __name__ == "__main__":
    typer.run(main)

# usage:
# python3.10 18_optionalCLIargumentDynamic.py --help
# use default values
# python3.10 18_optionalCLIargumentDynamic.py
# use your own value
# python3.10 18_optionalCLIargumentDynamic.py abc
