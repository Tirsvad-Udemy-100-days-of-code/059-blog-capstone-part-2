"""
@file
@brief Unit tests: the use cases, with a fake repository.
"""

import pytest

from blog.application.use_cases import get_post, get_posts
from blog.domain.errors import PostNotFoundError
from blog.domain.post import Post


def make_post(post_id: int) -> Post:
    """@brief Build a post with the given id."""
    return Post(post_id, f"Title {post_id}", "Sub", "Ann", "Today", "Body", "http://x/i.jpg")


class FakeRepository:
    """@brief In-memory PostRepository."""

    def __init__(self, posts: list[Post]) -> None:
        self._posts = posts

    def fetch_posts(self) -> list[Post]:
        """@brief Return the stored posts."""
        return self._posts


def test_get_posts_returns_all_posts() -> None:
    """@brief get_posts returns what the repository holds."""
    posts = [make_post(1), make_post(2)]
    assert get_posts(FakeRepository(posts)) == posts


def test_get_post_returns_matching_post() -> None:
    """@brief get_post finds a post by id."""
    assert get_post(FakeRepository([make_post(1), make_post(2)]), 2).id == 2


def test_get_post_raises_when_missing() -> None:
    """@brief An unknown id raises PostNotFoundError."""
    with pytest.raises(PostNotFoundError):
        get_post(FakeRepository([make_post(1)]), 999)
