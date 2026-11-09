[English](Step-4-Jinja-Include) · **Dansk** · [Bahasa Malaysia](Step-4-Jinja-Include-ms)

# Trin 4: del header og footer

Head, navigationslinjen og footeren er ens på alle sider. De ligger i `header.html` og `footer.html`, og hver side inkluderer dem.

![index.html med include-linjerne][step-4]

```html
{% include "header.html" %}
  ... the changeable part of the page ...
{% include "footer.html" %}
```

Sitet ser nøjagtigt ud som før; kun filerne er ændret.

## Hvad vi har lært

- Jinja `include` fjerner kopiér og indsæt: ret navigationen ét sted, og alle sider følger med.
- Siderne skrumper ind til den del, der virkelig er forskellig.
- Kontekst som `site_name` (fra `constants.APP_NAME`) er også synlig i inkluderede templates.

---

[step-4]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/059-blog-capstone-part-2/raw/branch/main/docs/screenshots/step-4-includes.png
