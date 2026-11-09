[English](Step-5-About-and-Contact) · [Dansk](Step-5-About-and-Contact-da) · **Bahasa Malaysia**

# Langkah 5: halaman About dan Contact

Pautan "Sample Post" dibuang daripada navigasi dan pautan lain menuju ke route, bukan ke fail.

![Halaman About][step-5a]
![Halaman Contact][step-5b]

```html
<a class="nav-link" href="{{ url_for('about') }}">About</a>
<a class="nav-link" href="{{ url_for('contact') }}">Contact</a>
```

```python
app.add_url_rule("/about", endpoint="about", view_func=about)
app.add_url_rule("/contact", endpoint="contact", view_func=contact)
```

Setiap halaman menetapkan imej pengepalanya sendiri dengan `url_for('static', filename='assets/img/about-bg.jpg')` dan `contact-bg.jpg` yang sepadan. Borang hubungan hanyalah susun atur templat; penghantaran mesej bukan sebahagian daripada pelajaran ini.

## Apa yang kita pelajari

- `url_for('about')` menggunakan nama endpoint, jadi menukar nama URL tidak akan merosakkan pautan.
- Setiap halaman menggunakan semula pengepala dan pengaki yang sama tanpa kerja tambahan.
- Ujian integrasi dengan klien ujian Flask menyemak bahawa ketiga-tiga halaman menjawab 200 dan pautannya betul.

---

[step-5a]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/059-blog-capstone-part-2/raw/branch/main/docs/screenshots/step-5-about.png
[step-5b]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/059-blog-capstone-part-2/raw/branch/main/docs/screenshots/step-5-contact.png
