"""
@file
@brief Unit tests: the JSON parser and the post repositories (no network).
"""

import json
import logging
from urllib.error import URLError

import pytest

from blog import constants
from blog.infrastructure import api_post_repository as module
from blog.infrastructure.api_post_repository import (
    ApiPostRepository,
    BundledPostRepository,
    parse_posts,
)

PAYLOAD = json.dumps(
    [
        {
            "id": "7",
            "title": "T",
            "subtitle": "S",
            "author": "Ann",
            "date": "May 1, 2024",
            "body": "B",
            "image_url": "http://x/i.jpg",
        }
    ]
).encode()


def test_parse_posts_converts_string_id_to_int() -> None:
    """@brief A string id becomes an int and fields are mapped."""
    post = parse_posts(PAYLOAD)[0]
    assert (post.id, post.title, post.author, post.date) == (7, "T", "Ann", "May 1, 2024")


def test_parse_posts_uses_defaults_for_missing_author_and_date() -> None:
    """@brief Missing author and date get the defaults."""
    raw = json.dumps([{"id": 1, "title": "T", "subtitle": "S", "body": "B", "image_url": "u"}])
    post = parse_posts(raw)[0]
    assert post.author == constants.DEFAULT_AUTHOR
    assert post.date == constants.DEFAULT_DATE


def test_parse_posts_rejects_post_without_title() -> None:
    """@brief A post missing a required field raises ValueError."""
    with pytest.raises(ValueError, match="invalid post"):
        parse_posts('[{"id": 1}]')


def test_api_repository_returns_posts_from_fetch() -> None:
    """@brief On success the fetched posts are returned, with the configured URL and timeout."""
    calls: list[tuple[str, int]] = []

    def fetch(url: str, timeout: int) -> bytes:
        calls.append((url, timeout))
        return PAYLOAD

    posts = ApiPostRepository(fetch).fetch_posts()
    assert [p.id for p in posts] == [7]
    assert calls == [(constants.POSTS_API_URL, constants.REQUEST_TIMEOUT_SECONDS)]


def test_api_repository_falls_back_on_url_error(caplog: pytest.LogCaptureFixture) -> None:
    """@brief A URLError gives the bundled posts and a warning."""

    def fetch(url: str, timeout: int) -> bytes:
        raise URLError("down")

    with caplog.at_level(logging.WARNING):
        posts = ApiPostRepository(fetch).fetch_posts()
    assert posts == BundledPostRepository().fetch_posts()
    assert "bundled" in caplog.text


@pytest.mark.parametrize("error", [TimeoutError(), OSError("x")])
def test_api_repository_falls_back_on_timeout_or_os_error(error: Exception) -> None:
    """@brief Timeouts and OS errors give the bundled posts."""

    def fetch(url: str, timeout: int) -> bytes:
        raise error

    assert ApiPostRepository(fetch).fetch_posts() == BundledPostRepository().fetch_posts()


def test_api_repository_falls_back_on_bad_json() -> None:
    """@brief Malformed JSON gives the bundled posts."""

    def fetch(url: str, timeout: int) -> bytes:
        return b"<html>not json"

    assert ApiPostRepository(fetch).fetch_posts() == BundledPostRepository().fetch_posts()


def test_bundled_repository_reads_the_bundled_file() -> None:
    """@brief The bundled posts are non-empty and start with the cactus post."""
    posts = BundledPostRepository().fetch_posts()
    assert posts
    assert (posts[0].id, posts[0].title) == (1, "The Life of Cactus")


def test_default_fetch_reads_url_with_timeout(monkeypatch: pytest.MonkeyPatch) -> None:
    """@brief urlopen_fetch passes the timeout and closes the response (no socket opened)."""
    seen: dict[str, object] = {}

    class FakeResponse:
        def __enter__(self) -> "FakeResponse":
            return self

        def __exit__(self, *args: object) -> None:
            seen["closed"] = True

        def read(self) -> bytes:
            return b"[]"

    def fake_urlopen(url: str, timeout: int) -> FakeResponse:
        seen["args"] = (url, timeout)
        return FakeResponse()

    monkeypatch.setattr(module, "urlopen", fake_urlopen)
    assert module.urlopen_fetch("http://h", 3) == b"[]"
    assert seen == {"args": ("http://h", 3), "closed": True}
