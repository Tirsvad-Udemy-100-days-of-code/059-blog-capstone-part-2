**English** · [Dansk](Step-3-Static-Files-da) · [Bahasa Malaysia](Step-3-Static-Files-ms)

# Step 3: fixing the static files

The template links to `css/styles.css` and `assets/img/home-bg.jpg` relative to the HTML file. Flask serves them under `/static`, so the links must be built with `url_for`.

![The styled home page with the background image][step-3]

```html
<link href="{{ url_for('static', filename='css/styles.css') }}" rel="stylesheet" />
<header class="masthead"
        style="background-image: url('{{ url_for('static', filename='assets/img/home-bg.jpg') }}')">
<script src="{{ url_for('static', filename='js/scripts.js') }}"></script>
```

With the footer script working, the navigation bar slides away when you scroll down and returns when you scroll up.

## What we gained

- `url_for('static', filename=...)` builds the right URL wherever the app is mounted.
- The Bootstrap styling, the navbar behaviour and the header image all depend on getting these paths right.
- A test (`tests/unit/test_templates.py`) now fails if a hard-coded `css/`, `js/` or `assets/` path creeps back in.

---

[step-3]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/059-blog-capstone-part-2/raw/branch/main/docs/screenshots/step-3-styled-home.png
