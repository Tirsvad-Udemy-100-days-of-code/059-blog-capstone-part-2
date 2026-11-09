"""
@file
@brief Smoke test: the package imports and its constants are sane.
"""

import sys

import blog
from blog import constants


def test_package_imports_and_has_docstring() -> None:
    """@brief The blog package is importable and documented."""
    assert blog.__doc__


def test_port_is_int() -> None:
    """@brief PORT is an integer."""
    assert isinstance(constants.PORT, int)


def test_posts_api_url_uses_https() -> None:
    """@brief The posts endpoint is reached over HTTPS."""
    assert constants.POSTS_API_URL.startswith("https://")


def test_python_version_is_at_least_3_13() -> None:
    """@brief The interpreter satisfies requires-python >= 3.13."""
    assert sys.version_info >= (3, 13)
