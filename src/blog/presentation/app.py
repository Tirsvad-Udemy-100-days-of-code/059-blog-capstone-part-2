"""
@file
@package blog.presentation.app
@brief Flask composition root: builds the app, its context and its routes.
"""

from flask import Flask, abort, render_template

from blog import constants
from blog.application.ports import PostRepository
from blog.application.use_cases import get_post, get_posts
from blog.domain.errors import PostNotFoundError
from blog.infrastructure.api_post_repository import ApiPostRepository


def about() -> str:
    """@brief Render the about page.

    @return The HTML of the about page.
    """
    return render_template("about.html")


def contact() -> str:
    """@brief Render the contact page.

    @return The HTML of the contact page.
    """
    return render_template("contact.html")


def inject_site_name() -> dict[str, str]:
    """@brief Make the site name available to every template.

    @return The template context with `site_name`.
    """
    return {"site_name": constants.APP_NAME}


def create_app(repository: PostRepository | None = None) -> Flask:
    """@brief Build the Flask application (the composition root).

    @param repository Source of posts; the remote API with bundled fallback when omitted.
    @return The configured application.
    """
    posts_source = repository if repository is not None else ApiPostRepository()

    def home() -> str:
        """@brief Render the home page with every post.

        @return The HTML of the home page.
        """
        return render_template("index.html", posts=get_posts(posts_source))

    def show_post(index: int) -> str:
        """@brief Render one post.

        @param index Id of the post.
        @return The HTML of the post page; answers 404 when it does not exist.
        """
        try:
            post = get_post(posts_source, index)
        except PostNotFoundError:
            abort(404)
        return render_template("post.html", post=post)

    app = Flask(__name__)
    app.context_processor(inject_site_name)
    app.add_url_rule("/", endpoint="home", view_func=home)
    app.add_url_rule("/post/<int:index>", endpoint="show_post", view_func=show_post)
    app.add_url_rule("/about", endpoint="about", view_func=about)
    app.add_url_rule("/contact", endpoint="contact", view_func=contact)
    return app
