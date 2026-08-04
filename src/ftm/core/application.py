from __future__ import annotations

from ftm.core.constants import APP_NAME
from ftm.core.version import __version__


class Application:
    """Main application."""

    def run(self) -> None:
        """Run application."""

        print()

        print(APP_NAME)

        print(f"Version: {__version__}")

        print()

        print("Application started successfully.")
