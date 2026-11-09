"""
@file
@package blog.infrastructure.api_post_repository
@brief Post repositories: the remote JSON API with a bundled-file fallback.
"""

import json
import logging
from collections.abc import Callable
from importlib import resources
from typing import Any
from urllib.error import URLError
from urllib.request import urlopen

from blog import constants
from blog.domain.post import Post

logger = logging.getLogger(__name__)

Fetch = Callable[[str, int], bytes]
"""@brief Reads a URL with a timeout in seconds and returns the response body."""


def parse_posts(raw: bytes | str) -> list[Post]:
    """@brief Map the JSON text of the posts to domain posts.

    @param raw JSON list of post objects.
    @return The posts; a missing author or date gets its default.
    @throws ValueError When the JSON is malformed or a post lacks a required field.
    """
    items: list[dict[str, Any]] = json.loads(raw)
    return [_to_post(item) for item in items]


def _to_post(item: dict[str, Any]) -> Post:
    try:
        return Post(
            id=int(item["id"]),
            title=item["title"],
            subtitle=item["subtitle"],
            author=item.get("author", constants.DEFAULT_AUTHOR),
            date=item.get("date", constants.DEFAULT_DATE),
            body=item["body"],
            image_url=item["image_url"],
        )
    except (KeyError, TypeError) as error:
        raise ValueError(f"invalid post: {item!r}") from error


def urlopen_fetch(url: str, timeout: int) -> bytes:
    """@brief Download a URL.

    @param url Address to read.
    @param timeout Seconds to wait before giving up.
    @return The response body.
    """
    with urlopen(url, timeout=timeout) as response:
        body: bytes = response.read()
    return body


def read_bundled_posts() -> list[Post]:
    """@brief Read the posts bundled with the package.

    @return The bundled posts.
    """
    data = resources.files("blog.infrastructure").joinpath("data", constants.POSTS_FALLBACK_FILE)
    return parse_posts(data.read_text(encoding="utf-8"))


class BundledPostRepository:
    """@brief Serves only the bundled posts; deterministic, no network."""

    def fetch_posts(self) -> list[Post]:
        """@brief Read every bundled post.

        @return All bundled posts.
        """
        return read_bundled_posts()


class ApiPostRepository:
    """@brief Serves posts from the remote API, falling back to the bundled file."""

    def __init__(self, fetch: Fetch = urlopen_fetch) -> None:
        """@brief Create the repository.

        @param fetch Function that downloads a URL; replaced in tests.
        """
        self._fetch = fetch

    def fetch_posts(self) -> list[Post]:
        """@brief Read the posts from the API, or the bundled file when it fails.

        @return All posts.
        """
        try:
            return parse_posts(
                self._fetch(constants.POSTS_API_URL, constants.REQUEST_TIMEOUT_SECONDS)
            )
        except (URLError, OSError, TimeoutError, ValueError) as error:
            # JSONDecodeError is a ValueError.
            logger.warning("Posts API unavailable (%s); using the bundled posts", error)
            return read_bundled_posts()
