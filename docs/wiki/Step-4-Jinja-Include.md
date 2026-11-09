**English** · [Dansk](Step-4-Jinja-Include-da) · [Bahasa Malaysia](Step-4-Jinja-Include-ms)

# Step 4: sharing the header and footer

The head, the navigation bar and the footer are the same on every page. They live in `header.html` and `footer.html` and each page includes them.

![index.html with the include lines][step-4]

```html
{% include "header.html" %}
  ... the changeable part of the page ...
{% include "footer.html" %}
```

The site looks exactly as before; only the files changed.

## What we gained

- Jinja `include` removes copy and paste: change the navigation once and every page follows.
- Pages shrink to the part that is really different.
- Context such as `site_name` (from `constants.APP_NAME`) is visible in included templates too.

---

[step-4]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/059-blog-capstone-part-2/raw/branch/main/docs/screenshots/step-4-includes.png
