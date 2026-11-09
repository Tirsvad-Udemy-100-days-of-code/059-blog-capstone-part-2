**English** · [Dansk](Step-5-About-and-Contact-da) · [Bahasa Malaysia](Step-5-About-and-Contact-ms)

# Step 5: the About and Contact pages

The "Sample Post" link is removed from the navigation and the other links point at routes, not at files.

![The About page][step-5a]
![The Contact page][step-5b]

```html
<a class="nav-link" href="{{ url_for('about') }}">About</a>
<a class="nav-link" href="{{ url_for('contact') }}">Contact</a>
```

```python
app.add_url_rule("/about", endpoint="about", view_func=about)
app.add_url_rule("/contact", endpoint="contact", view_func=contact)
```

Each page sets its own header image with `url_for('static', filename='assets/img/about-bg.jpg')` and the matching `contact-bg.jpg`. The contact form is only the template's layout; sending messages is not part of this lesson.

## What we gained

- `url_for('about')` uses the endpoint name, so renaming a URL never breaks a link.
- Every page reuses the same header and footer with no extra work.
- Integration tests with Flask's test client check that all three pages answer 200 and that the links are right.

---

[step-5a]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/059-blog-capstone-part-2/raw/branch/main/docs/screenshots/step-5-about.png
[step-5b]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/059-blog-capstone-part-2/raw/branch/main/docs/screenshots/step-5-contact.png
