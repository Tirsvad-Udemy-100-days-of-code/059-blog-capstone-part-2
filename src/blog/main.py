"""
@file
@package blog.main
@brief Entry point: runs the development server (`python -m blog.main`).
"""

from blog import constants
from blog.presentation.app import create_app

app = create_app()


def main() -> None:
    """@brief Start the development server on the configured host and port."""
    app.run(host=constants.HOST, port=constants.PORT)


if __name__ == "__main__":
    main()
