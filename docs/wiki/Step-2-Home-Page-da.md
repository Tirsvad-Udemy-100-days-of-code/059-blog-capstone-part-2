[English](Step-2-Home-Page) · **Dansk** · [Bahasa Malaysia](Step-2-Home-Page-ms)

# Trin 2: forsiden

En route er en funktion knyttet til en URL. Funktionen `home` renderer `index.html`, når du åbner `http://localhost:5000`.

![Forsiden før CSS og JavaScript indlæses][step-2]

```python
app.add_url_rule("/", endpoint="home", view_func=home)

def home() -> str:
    return render_template("index.html")
```

Skærmbilledet viser siden, hvor alle forespørgsler efter CSS, skrifttyper og scripts er blokeret. Sådan ser siden ud, når ressourcerne ikke findes: indholdet er der, men stylingen mangler.

## Hvad vi har lært

- `render_template` læser en fil fra `templates` og returnerer HTML.
- En side kan indlæses og alligevel se ødelagt ud: HTML og dens ressourcer er separate forespørgsler.
- Opgavens funktionsnavn `home` er bevaret, så du kan sammenligne din løsning med denne.

---

[step-2]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/059-blog-capstone-part-2/raw/branch/main/docs/screenshots/step-2-unstyled-home.png
