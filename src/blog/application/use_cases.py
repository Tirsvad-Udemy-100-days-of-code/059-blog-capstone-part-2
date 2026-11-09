"""
@file
@package blog.application.use_cases
@brief The use cases of the blog.
"""

from blog.application.ports import PostRepository
from blog.domain.errors import PostNotFoundError
from blog.domain.post import Post


def get_posts(repository: PostRepository) -> list[Post]:
    """@brief List every post.

    @param repository Source of posts.
    @return All posts.
    """
    return repository.fetch_posts()


def get_post(repository: PostRepository, post_id: int) -> Post:
    """@brief Find one post by id.

    @param repository Source of posts.
    @param post_id Id of the wanted post.
    @return The post with that id.
    @throws PostNotFoundError When no post has that id.
    """
    for post in repository.fetch_posts():
        if post.id == post_id:
            return post
    raise PostNotFoundError(post_id)
