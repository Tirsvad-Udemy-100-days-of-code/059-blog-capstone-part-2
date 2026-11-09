"""
@file
@package blog.infrastructure.api_post_repository
@brief Post repositories: the remote JSON API with a bundled-file fallback.
"""

import json
import logging
from collections.abc import Callable

# False positive: the project requires Python >=3.13, where importlib.resources exists.
# nosemgrep: opengrep.rules.python.lang.compatibility.python37-compatibility-importlib2
from importlib import resources
from typing import Any
from urllib.error import URLError
from urllib.parse import urlsplit
from urllib.request import urlopen

from blog import constants
from blog.domain.post import Post

logger = logging.getLogger(__name__)

ALLOWED_URL_SCHEMES = frozenset({"http", "https"})
"""@brief URL schemes urlopen_fetch may open; urllib would also open file: and ftp:."""

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
    @throws ValueError When the URL scheme is not http or https.
    """
    scheme = urlsplit(url).scheme
    if scheme not in ALLOWED_URL_SCHEMES:
        raise ValueError(f"unsupported URL scheme: {scheme!r}")
    # Scheme restricted to http/https above.
    # nosemgrep: opengrep.rules.python.lang.security.audit.dynamic-urllib-use-detected
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
