**English** · [Dansk](Home-da) · [Bahasa Malaysia](Home-ms)

# Blog Capstone Part 2 (Day 59)

This wiki explains the Day 59 project of Udemy's "100 Days of Code: The Complete Python Pro Bootcamp": a Flask blog upgraded with the Start Bootstrap "Clean Blog" template. Every lecture step has a page with a screenshot, the code that matters and a section "What we gained".

## What you build

- A multi-page site with a navigation bar that adapts to small screens.
- A header and a footer written once and shared with Jinja `include`.
- Blog posts fetched from a JSON API and shown on the home page.
- One page per post with a full-width title image.

## The seven steps

| Step | Page | You learn |
| --- | --- | --- |
| 1 | [Step-1-Template-and-Folders](Step-1-Template-and-Folders) | How a Flask project separates `templates` and `static` |
| 2 | [Step-2-Home-Page](Step-2-Home-Page) | Serving a page from a route |
| 3 | [Step-3-Static-Files](Step-3-Static-Files) | `url_for('static', ...)` for CSS, JavaScript and images |
| 4 | [Step-4-Jinja-Include](Step-4-Jinja-Include) | Sharing a header and footer with `include` |
| 5 | [Step-5-About-and-Contact](Step-5-About-and-Contact) | More routes and links built with `url_for` |
| 6 | [Step-6-Posts-from-API](Step-6-Posts-from-API) | Reading JSON from an API and looping in Jinja |
| 7 | [Step-7-Single-Post](Step-7-Single-Post) | A route with a variable part and a 404 |

Start with [Getting-Started](Getting-Started) to run the site yourself.

## The project at a glance

The code follows a light Clean Architecture: `domain` (the `Post`), `application` (the use cases `get_posts` and `get_post`), `infrastructure` (reading the API) and `presentation` (Flask routes, templates and static files). All constants are in `src/blog/constants.py`. Flask is the only runtime dependency.

[Repository](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/059-blog-capstone-part-2) · [Issue tracker](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/059-blog-capstone-part-2/issues)
