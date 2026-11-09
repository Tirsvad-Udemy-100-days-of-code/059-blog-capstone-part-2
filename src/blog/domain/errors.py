"""
@file
@package blog.domain.errors
@brief Errors raised by the business rules.
"""


class PostNotFoundError(LookupError):
    """@brief Raised when no post has the requested id."""
