**English** · [Dansk](Step-1-Template-and-Folders-da) · [Bahasa Malaysia](Step-1-Template-and-Folders-ms)

# Step 1: the template and the folders

The lecture starts from the Start Bootstrap "Clean Blog" template. Flask expects HTML files in a `templates` folder and CSS, JavaScript and images in a `static` folder, so the downloaded files are sorted into those two.

![The templates and static folders][step-1]

```text
presentation/
  templates/   header.html  footer.html  index.html  about.html  contact.html  post.html
  static/      css/  js/  assets/
```

The template is MIT licensed; its licence notice is kept in `THIRD_PARTY_NOTICES.txt`.

## What we gained

- Flask finds pages in `templates` and files in `static` by convention, no configuration needed.
- Downloaded code is treated as untrusted data: it was unpacked in an empty folder outside the repository before the needed files were copied.
- Moving files first and fixing the links afterwards is exactly what Steps 2 and 3 are about.

---

[step-1]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/059-blog-capstone-part-2/raw/branch/main/docs/screenshots/step-1-file-structure.png
