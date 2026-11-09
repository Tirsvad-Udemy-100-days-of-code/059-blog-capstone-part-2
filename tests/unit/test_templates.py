"""
@file
@brief Unit tests: template structure (no hard-coded asset paths, shared includes).
"""

import re
from pathlib import Path

import pytest

TEMPLATES = Path(__file__).resolve().parents[2] / "src/blog/presentation/templates"
PAGES = ["index.html", "post.html", "about.html", "contact.html"]


def _read(name: str) -> str:
    return (TEMPLATES / name).read_text(encoding="utf-8")


@pytest.mark.parametrize("name", ["header.html", "footer.html", *PAGES])
def test_assets_go_through_url_for(name: str) -> None:
    """@brief No href/src points to a literal local asset path."""
    text = _read(name)
    assert not re.search(r"""(?:href|src)=["'](?:/?static/|css/|js/|assets/)""", text)


@pytest.mark.parametrize("name", ["header.html", "footer.html", *PAGES])
def test_no_href_ends_in_html(name: str) -> None:
    """@brief Links use url_for, never a .html file."""
    assert not re.search(r"""href=["'][^"']*\.html["']""", _read(name))


@pytest.mark.parametrize("name", PAGES)
def test_page_includes_header_and_footer(name: str) -> None:
    """@brief Pages share the header and footer through includes."""
    text = _read(name)
    assert '{% include "header.html" %}' in text
    assert '{% include "footer.html" %}' in text


@pytest.mark.parametrize("name", PAGES)
def test_page_has_no_own_footer_or_head(name: str) -> None:
    """@brief Page templates do not repeat the shared markup."""
    text = _read(name)
    assert "<footer" not in text
    assert not re.search(r"<head[\s>]", text)
