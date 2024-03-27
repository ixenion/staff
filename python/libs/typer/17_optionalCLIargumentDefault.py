import typer


def main(name: str = typer.Argument("Wade Wilson")):
    print(f"Hello {name}")


if __name__ == "__main__":
    typer.run(main)

# usage:
# $ python3.10 ... --help
# default
# $ python3.10 ...
# use your own value
# python3.10 ... abc

