"""
@file
@brief Integration tests: the post pages served by Flask with a fake repository.
"""

import pytest
from flask.testing import FlaskClient

from blog.domain.post import Post
from blog.presentation.app import create_app

POSTS = [
    Post(
        1, "First <b>Title</b>", "First sub", "Ann", "May 1, 2024", "First body", "http://x/a.jpg"
    ),
    Post(2, "Second Title", "Second sub", "Bob", "June 2, 2024", "Second body", "http://x/b.jpg"),
]


class FakeRepository:
    """@brief In-memory PostRepository."""

    def fetch_posts(self) -> list[Post]:
        """@brief Return the fixed posts."""
        return POSTS


@pytest.fixture
def client() -> FlaskClient:
    """@brief Test client of an app with fake posts."""
    return create_app(FakeRepository()).test_client()


def test_home_lists_every_post_with_link(client: FlaskClient) -> None:
    """@brief The home page shows titles, authors, dates and links to each post."""
    html = client.get("/").get_data(as_text=True)
    for text in (
        "Second Title",
        "Second sub",
        "Posted by Ann on May 1, 2024",
        "Bob",
        "June 2, 2024",
    ):
        assert text in html
    assert 'href="/post/1"' in html
    assert 'href="/post/2"' in html
    assert html.count('<hr class="my-4" />') == 1


def test_home_escapes_post_text(client: FlaskClient) -> None:
    """@brief HTML in a title is escaped."""
    html = client.get("/").get_data(as_text=True)
    assert "First &lt;b&gt;Title&lt;/b&gt;" in html


def test_post_page_shows_the_post(client: FlaskClient) -> None:
    """@brief /post/2 shows title, subtitle, author, date, body and image."""
    response = client.get("/post/2")
    html = response.get_data(as_text=True)
    assert response.status_code == 200
    for text in ("Second Title", "Second sub", "Posted by Bob on June 2, 2024", "Second body"):
        assert text in html
    assert "http://x/b.jpg" in html


def test_unknown_post_returns_404(client: FlaskClient) -> None:
    """@brief /post/999 answers 404."""
    assert client.get("/post/999").status_code == 404
