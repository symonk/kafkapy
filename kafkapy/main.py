import typer


def main(name: str):
    """Entry point to kafkapy."""

    typer.Exit(code=0)


if __name__ == "__main__":
    typer.run(main)