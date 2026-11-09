[English](Step-1-Template-and-Folders) · [Dansk](Step-1-Template-and-Folders-da) · **Bahasa Malaysia**

# Langkah 1: templat dan folder

Kuliah bermula daripada templat Start Bootstrap "Clean Blog". Flask mengharapkan fail HTML berada dalam folder `templates` serta CSS, JavaScript dan imej dalam folder `static`, jadi fail yang dimuat turun diasingkan ke dalam kedua-dua folder tersebut.

![Folder templates dan static][step-1]

```text
presentation/
  templates/   header.html  footer.html  index.html  about.html  contact.html  post.html
  static/      css/  js/  assets/
```

Templat ini berlesen MIT; notis lesennya disimpan dalam `THIRD_PARTY_NOTICES.txt`.

## Apa yang kita pelajari

- Flask mencari halaman dalam `templates` dan fail dalam `static` mengikut konvensyen, tanpa perlu sebarang konfigurasi.
- Kod yang dimuat turun dianggap sebagai data yang tidak dipercayai: ia diekstrak dalam folder kosong di luar repositori sebelum fail yang diperlukan disalin.
- Memindahkan fail dahulu dan membetulkan pautan kemudian ialah tepat apa yang dibincangkan dalam Langkah 2 dan 3.

---

[step-1]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/059-blog-capstone-part-2/raw/branch/main/docs/screenshots/step-1-file-structure.png
