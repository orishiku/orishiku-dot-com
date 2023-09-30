import typer
from typing import Optional

from common.commands import app

cli = typer.Typer()


@cli.command()
def run():
    app.run()

@cli.command()
def migrate():
    app.run()

if __name__ == "__main__":
    cli()
