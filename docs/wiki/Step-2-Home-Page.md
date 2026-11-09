**English** · [Dansk](Step-2-Home-Page-da) · [Bahasa Malaysia](Step-2-Home-Page-ms)

# Step 2: the home page

A route is a function tied to a URL. The `home` function renders `index.html` when you open `http://localhost:5000`.

![The home page before the CSS and JavaScript load][step-2]

```python
app.add_url_rule("/", endpoint="home", view_func=home)

def home() -> str:
    return render_template("index.html")
```

The screenshot shows the page with every CSS, font and script request blocked, which is how the page looks when the assets are not found: the content is there, the styling is missing.

## What we gained

- `render_template` reads a file from `templates` and returns HTML.
- A page can load and still look broken: the HTML and its assets are separate requests.
- The assignment's function name `home` is kept, so you can compare your solution with this one.

---

[step-2]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/059-blog-capstone-part-2/raw/branch/main/docs/screenshots/step-2-unstyled-home.png
