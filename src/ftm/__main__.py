from __future__ import annotations

import typer

from ftm.main import run

app = typer.Typer(
    add_completion=False,
    no_args_is_help=False,
)


@app.callback(invoke_without_command=True)
def main() -> None:
    """Family Time Manager."""

    run()


if __name__ == "__main__":
    app()
