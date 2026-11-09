"""
@file
@package blog.domain.post
@brief The blog post entity.
"""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Post:
    """@brief One blog post; immutable."""

    id: int
    title: str
    subtitle: str
    author: str
    date: str
    body: str
    image_url: str
