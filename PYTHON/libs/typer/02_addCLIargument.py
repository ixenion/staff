# usage:
# $ python3.10 02..py
# $ python3.10 02..py --help

import typer

def main(name: str):
    print(f"Hello {name}")

if __name__ == "__main__":
    typer.run(main)

