"""
@file
@package blog.presentation.app
@brief Flask composition root: builds the app, its context and its routes.
"""

from flask import Flask, render_template

from blog import constants


def home() -> str:
    """@brief Render the home page.

    @return The HTML of the home page.
    """
    return render_template("index.html")


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


def create_app() -> Flask:
    """@brief Build the Flask application.

    @return The configured application.
    """
    app = Flask(__name__)
    app.context_processor(inject_site_name)
    app.add_url_rule("/", endpoint="home", view_func=home)
    app.add_url_rule("/about", endpoint="about", view_func=about)
    app.add_url_rule("/contact", endpoint="contact", view_func=contact)
    return app
