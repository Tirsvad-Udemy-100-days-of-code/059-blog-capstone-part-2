"""
@file
@brief Integration tests: the pages and static files are served by the Flask app.
"""

import re

import pytest
from flask.testing import FlaskClient

from blog import constants
from blog.presentation.app import create_app


@pytest.fixture
def client() -> FlaskClient:
    """@brief Test client of a fresh app."""
    return create_app().test_client()


@pytest.mark.parametrize("path", ["/", "/about", "/contact"])
def test_page_returns_200_with_site_name(client: FlaskClient, path: str) -> None:
    """@brief Each page answers 200 and shows the site name."""
    response = client.get(path)
    assert response.status_code == 200
    assert constants.APP_NAME in response.get_data(as_text=True)


def test_navigation_links_point_to_the_routes(client: FlaskClient) -> None:
    """@brief The header links to /, /about and /contact."""
    html = client.get("/").get_data(as_text=True)
    hrefs = re.findall(r'href="(/[^"]*)"', html)
    for route in ("/", "/about", "/contact"):
        assert route in hrefs


def test_header_has_no_sample_post_link(client: FlaskClient) -> None:
    """@brief The sample post is not linked from the navigation."""
    html = client.get("/").get_data(as_text=True)
    assert "post.html" not in html
    assert "Sample Post" not in html


@pytest.mark.parametrize(
    "path",
    ["/static/css/styles.css", "/static/js/scripts.js", "/static/assets/img/home-bg.jpg"],
)
def test_static_file_returns_200(client: FlaskClient, path: str) -> None:
    """@brief Static assets are served under /static."""
    response = client.get(path)
    assert response.status_code == 200
    response.close()
