"""
@file
@package blog.application.ports
@brief Interfaces the use cases need from the outside world.
"""

from typing import Protocol

from blog.domain.post import Post


class PostRepository(Protocol):
    """@brief Source of blog posts."""

    def fetch_posts(self) -> list[Post]:
        """@brief Read every post.

        @return All posts, in source order.
        """
        ...
