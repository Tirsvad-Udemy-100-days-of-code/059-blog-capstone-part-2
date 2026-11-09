[English](Step-5-About-and-Contact) · **Dansk** · [Bahasa Malaysia](Step-5-About-and-Contact-ms)

# Trin 5: siderne Om og Kontakt

Linket "Sample Post" fjernes fra navigationen, og de øvrige links peger på routes, ikke på filer.

![Siden About][step-5a]
![Siden Contact][step-5b]

```html
<a class="nav-link" href="{{ url_for('about') }}">About</a>
<a class="nav-link" href="{{ url_for('contact') }}">Contact</a>
```

```python
app.add_url_rule("/about", endpoint="about", view_func=about)
app.add_url_rule("/contact", endpoint="contact", view_func=contact)
```

Hver side sætter sit eget headerbillede med `url_for('static', filename='assets/img/about-bg.jpg')` og det tilsvarende `contact-bg.jpg`. Kontaktformularen er kun skabelonens layout; at sende beskeder er ikke en del af denne lektion.

## Hvad vi har lært

- `url_for('about')` bruger endpoint-navnet, så omdøbning af en URL aldrig ødelægger et link.
- Hver side genbruger den samme header og footer uden ekstra arbejde.
- Integrationstests med Flasks testklient kontrollerer, at alle tre sider svarer 200, og at linkene er rigtige.

---

[step-5a]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/059-blog-capstone-part-2/raw/branch/main/docs/screenshots/step-5-about.png
[step-5b]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/059-blog-capstone-part-2/raw/branch/main/docs/screenshots/step-5-contact.png
