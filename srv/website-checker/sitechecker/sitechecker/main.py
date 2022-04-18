import typer


def main(filename: str, period_min: int):
    typer.echo(f"Filename {filename}, period in minutes {period_min}")


def run():
    typer.run(main)


if __name__ == "__main__":
    run()