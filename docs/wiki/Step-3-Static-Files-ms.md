[English](Step-3-Static-Files) · [Dansk](Step-3-Static-Files-da) · **Bahasa Malaysia**

# Langkah 3: membetulkan fail statik

Templat memaut ke `css/styles.css` dan `assets/img/home-bg.jpg` secara relatif kepada fail HTML. Flask menghidangkannya di bawah `/static`, jadi pautan mesti dibina dengan `url_for`.

![Halaman utama yang bergaya dengan imej latar belakang][step-3]

```html
<link href="{{ url_for('static', filename='css/styles.css') }}" rel="stylesheet" />
<header class="masthead"
        style="background-image: url('{{ url_for('static', filename='assets/img/home-bg.jpg') }}')">
<script src="{{ url_for('static', filename='js/scripts.js') }}"></script>
```

Apabila skrip pengaki berfungsi, bar navigasi meluncur pergi apabila anda menatal ke bawah dan kembali apabila anda menatal ke atas.

## Apa yang kita pelajari

- `url_for('static', filename=...)` membina URL yang betul walau di mana pun aplikasi dipasang.
- Gaya Bootstrap, kelakuan navbar dan imej pengepala semuanya bergantung pada laluan yang betul.
- Ujian (`tests/unit/test_templates.py`) kini gagal jika laluan `css/`, `js/` atau `assets/` yang ditulis terus muncul semula.

---

[step-3]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/059-blog-capstone-part-2/raw/branch/main/docs/screenshots/step-3-styled-home.png
