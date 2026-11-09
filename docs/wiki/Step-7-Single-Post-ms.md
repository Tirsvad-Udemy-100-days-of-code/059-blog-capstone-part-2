[English](Step-7-Single-Post) · [Dansk](Step-7-Single-Post-da) · **Bahasa Malaysia**

# Langkah 7: satu halaman bagi setiap catatan

Mengklik tajuk membuka `/post/<id>`, yang memaparkan tajuk, subtajuk, penulis, tarikh dan kandungan di atas imej selebar penuh.

![Halaman catatan untuk The Life of Cactus][step-7]

```python
app.add_url_rule("/post/<int:index>", endpoint="show_post", view_func=show_post)

def show_post(index: int) -> str:
    try:
        post = get_post(posts_source, index)
    except PostNotFoundError:
        abort(404)
    return render_template("post.html", post=post)
```

## Apa yang kita pelajari

- URL boleh membawa bahagian yang berubah: `<int:index>` ditukar kepada `int` untuk anda.
- Mencari sesuatu dan tidak menjumpainya ialah keadaan biasa: kes guna melemparkan `PostNotFoundError` dan route menjawab 404.
- `post.html` yang sama memaparkan setiap catatan, dan imej pengepala datang daripada `image_url` milik catatan itu sendiri.

---

[step-7]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/059-blog-capstone-part-2/raw/branch/main/docs/screenshots/step-7-post.png
