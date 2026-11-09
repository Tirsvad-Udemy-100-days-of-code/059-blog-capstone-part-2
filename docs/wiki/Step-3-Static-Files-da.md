[English](Step-3-Static-Files) · **Dansk** · [Bahasa Malaysia](Step-3-Static-Files-ms)

# Trin 3: ret de statiske filer

Skabelonen linker til `css/styles.css` og `assets/img/home-bg.jpg` relativt til HTML-filen. Flask leverer dem under `/static`, så linkene skal bygges med `url_for`.

![Den stylede forside med baggrundsbilledet][step-3]

```html
<link href="{{ url_for('static', filename='css/styles.css') }}" rel="stylesheet" />
<header class="masthead"
        style="background-image: url('{{ url_for('static', filename='assets/img/home-bg.jpg') }}')">
<script src="{{ url_for('static', filename='js/scripts.js') }}"></script>
```

Når footer-scriptet virker, glider navigationslinjen væk, når du ruller ned, og vender tilbage, når du ruller op.

## Hvad vi har lært

- `url_for('static', filename=...)` bygger den rigtige URL, uanset hvor appen er monteret.
- Bootstrap-stylingen, navigationslinjens adfærd og headerbilledet afhænger alle af, at disse stier er rigtige.
- En test (`tests/unit/test_templates.py`) fejler nu, hvis en hårdkodet sti til `css/`, `js/` eller `assets/` sniger sig tilbage.

---

[step-3]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/059-blog-capstone-part-2/raw/branch/main/docs/screenshots/step-3-styled-home.png
