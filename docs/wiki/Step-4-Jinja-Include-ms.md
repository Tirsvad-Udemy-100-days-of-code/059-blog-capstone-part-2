[English](Step-4-Jinja-Include) · [Dansk](Step-4-Jinja-Include-da) · **Bahasa Malaysia**

# Langkah 4: berkongsi pengepala dan pengaki

Bahagian head, bar navigasi dan pengaki adalah sama pada setiap halaman. Ia disimpan dalam `header.html` dan `footer.html` dan setiap halaman menyertakannya.

![index.html dengan baris include][step-4]

```html
{% include "header.html" %}
  ... the changeable part of the page ...
{% include "footer.html" %}
```

Laman web kelihatan sama seperti sebelumnya; hanya failnya yang berubah.

## Apa yang kita pelajari

- Jinja `include` menghapuskan salin dan tampal: ubah navigasi sekali dan setiap halaman akan mengikutinya.
- Halaman menjadi lebih ringkas, hanya bahagian yang benar-benar berbeza.
- Konteks seperti `site_name` (daripada `constants.APP_NAME`) turut kelihatan dalam templat yang disertakan.

---

[step-4]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/059-blog-capstone-part-2/raw/branch/main/docs/screenshots/step-4-includes.png
