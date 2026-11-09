[English](Step-1-Template-and-Folders) · **Dansk** · [Bahasa Malaysia](Step-1-Template-and-Folders-ms)

# Trin 1: skabelonen og mapperne

Forelæsningen tager udgangspunkt i Start Bootstraps skabelon "Clean Blog". Flask forventer HTML-filer i en mappe kaldet `templates` og CSS, JavaScript og billeder i en mappe kaldet `static`, så de downloadede filer sorteres i de to mapper.

![Mapperne templates og static][step-1]

```text
presentation/
  templates/   header.html  footer.html  index.html  about.html  contact.html  post.html
  static/      css/  js/  assets/
```

Skabelonen har MIT-licens; licensmeddelelsen opbevares i `THIRD_PARTY_NOTICES.txt`.

## Hvad vi har lært

- Flask finder sider i `templates` og filer i `static` efter konvention, uden nogen konfiguration.
- Downloadet kode behandles som upålidelige data: den blev pakket ud i en tom mappe uden for repositoryet, før de nødvendige filer blev kopieret.
- At flytte filer først og rette linkene bagefter er præcis det, trin 2 og 3 handler om.

---

[step-1]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/059-blog-capstone-part-2/raw/branch/main/docs/screenshots/step-1-file-structure.png
