"""Command-line interface."""

import click


@click.command()
@click.version_option()
def main() -> None:
    """Desssign."""


if __name__ == "__main__":
    main(prog_name="desssign")  # pragma: no cover
