[English](Step-7-Single-Post) · **Dansk** · [Bahasa Malaysia](Step-7-Single-Post-ms)

# Trin 7: én side pr. indlæg

Et klik på en titel åbner `/post/<id>`, som viser titel, undertitel, forfatter, dato og brødtekst over et billede i fuld bredde.

![Indlægssiden for The Life of Cactus][step-7]

```python
app.add_url_rule("/post/<int:index>", endpoint="show_post", view_func=show_post)

def show_post(index: int) -> str:
    try:
        post = get_post(posts_source, index)
    except PostNotFoundError:
        abort(404)
    return render_template("post.html", post=post)
```

## Hvad vi har lært

- En URL kan indeholde en variabel del: `<int:index>` konverteres automatisk til en `int`.
- At slå noget op og ikke finde det er et normalt tilfælde: use casen rejser `PostNotFoundError`, og routen svarer 404.
- Den samme `post.html` viser alle indlæg, og headerbilledet kommer fra indlæggets egen `image_url`.

---

[step-7]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/059-blog-capstone-part-2/raw/branch/main/docs/screenshots/step-7-post.png
