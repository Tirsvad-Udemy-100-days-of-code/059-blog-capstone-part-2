"""
@file
@package blog.constants
@brief Every constant of the project, defined once.
"""

from typing import Final

APP_NAME: Final[str] = "Clean Blog"
"""@brief Name shown in the page title and navigation bar."""

HOST: Final[str] = "127.0.0.1"
"""@brief Address the development server binds to."""

PORT: Final[int] = 5000
"""@brief Port the development server listens on."""

POSTS_API_URL: Final[str] = "https://api.npoint.io/674f5423f73deab1e9a7"
"""@brief Remote JSON endpoint that serves the blog posts."""

REQUEST_TIMEOUT_SECONDS: Final[int] = 5
"""@brief Seconds to wait for the posts endpoint before giving up."""

POSTS_FALLBACK_FILE: Final[str] = "posts.json"
"""@brief Local file used when the posts endpoint is unavailable."""
