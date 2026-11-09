[English](Step-2-Home-Page) · [Dansk](Step-2-Home-Page-da) · **Bahasa Malaysia**

# Langkah 2: halaman utama

Route ialah fungsi yang dikaitkan dengan sebuah URL. Fungsi `home` memaparkan `index.html` apabila anda membuka `http://localhost:5000`.

![Halaman utama sebelum CSS dan JavaScript dimuatkan][step-2]

```python
app.add_url_rule("/", endpoint="home", view_func=home)

def home() -> str:
    return render_template("index.html")
```

Tangkapan skrin menunjukkan halaman dengan setiap permintaan CSS, fon dan skrip disekat, iaitu rupa halaman apabila aset tidak ditemui: kandungan ada, tetapi gayanya tiada.

## Apa yang kita pelajari

- `render_template` membaca fail daripada `templates` dan memulangkan HTML.
- Sesebuah halaman boleh dimuatkan tetapi masih kelihatan rosak: HTML dan asetnya ialah permintaan yang berasingan.
- Nama fungsi `home` daripada tugasan dikekalkan, supaya anda boleh membandingkan penyelesaian anda dengan yang ini.

---

[step-2]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/059-blog-capstone-part-2/raw/branch/main/docs/screenshots/step-2-unstyled-home.png
