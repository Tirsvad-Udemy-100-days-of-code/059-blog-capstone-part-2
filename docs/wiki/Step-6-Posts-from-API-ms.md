[English](Step-6-Posts-from-API) · [Dansk](Step-6-Posts-from-API-da) · **Bahasa Malaysia**

# Langkah 6: catatan daripada API

Catatan tidak lagi ditaip terus ke dalam HTML. Ia ialah JSON yang dihidangkan oleh API dan dipaparkan dengan gelung Jinja `for`.

![Halaman utama yang menyenaraikan catatan][step-6]

```html
{% for post in posts %}
  <a href="{{ url_for('show_post', index=post.id) }}">
    <h2 class="post-title">{{ post.title }}</h2>
    <h3 class="post-subtitle">{{ post.subtitle }}</h3>
  </a>
  <p class="post-meta">Posted by {{ post.author }} on {{ post.date }}</p>
{% endfor %}
```

Data dibaca dengan pustaka standard (`urllib`), jadi projek ini tidak memerlukan `requests`. Jika API tidak dapat dicapai, salinan catatan contoh yang disertakan dalam pakej akan digunakan, supaya laman web dan ujian berfungsi tanpa talian. Catatan dihurai di satu tempat menjadi `Post`, dan kes guna `get_posts` menyerahkannya kepada route.

## Apa yang kita pelajari

- Tatatanda titik dalam Jinja (`post.title`) mudah dibaca; gelung yang sama berfungsi untuk sebarang bilangan catatan.
- Membaca daripada API ialah tanggungjawab yang berasingan: route tidak tahu dari mana catatan datang, jadi ujian menyuntik repositori palsu.
- Pilihan sandaran dan had masa (`REQUEST_TIMEOUT_SECONDS` dalam `constants.py`) memastikan halaman terus berfungsi apabila rangkaian tidak berfungsi.

---

[step-6]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/059-blog-capstone-part-2/raw/branch/main/docs/screenshots/step-6-home-posts.png
