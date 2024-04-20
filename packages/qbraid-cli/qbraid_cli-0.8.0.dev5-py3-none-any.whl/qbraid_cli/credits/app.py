# Copyright (c) 2024, qBraid Development Team
# All rights reserved.

"""
Module defining commands in the 'qbraid credits' namespace.

"""

import typer

from qbraid_cli.handlers import run_progress_task

credits_app = typer.Typer(help="Manage qBraid credits.")


@credits_app.command(name="value")
def credits_value():
    """Get number of qBraid credits remaining."""

    def get_credits() -> float:
        from qbraid_core import QbraidClient

        client = QbraidClient()
        return client.user_credits_value()

    qbraid_credits: float = run_progress_task(get_credits)
    credits_text = typer.style(f"{qbraid_credits:.2f}", fg=typer.colors.GREEN, bold=True)
    typer.secho(f"\nqBraid credits: {credits_text}")


if __name__ == "__main__":
    credits_app()
