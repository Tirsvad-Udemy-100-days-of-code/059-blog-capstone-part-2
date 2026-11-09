[English](Home) · [Dansk](Home-da) · **Bahasa Malaysia**

# Blog Capstone Part 2 (Hari 59)

Wiki ini menerangkan projek Hari 59 daripada kursus Udemy "100 Days of Code: The Complete Python Pro Bootcamp": sebuah blog Flask yang dinaik taraf dengan templat Start Bootstrap "Clean Blog". Setiap langkah kuliah mempunyai halaman dengan tangkapan skrin, kod yang penting dan bahagian "Apa yang kita pelajari".

## Apa yang anda bina

- Laman web berbilang halaman dengan bar navigasi yang menyesuaikan diri dengan skrin kecil.
- Pengepala dan pengaki yang ditulis sekali sahaja dan dikongsi dengan Jinja `include`.
- Catatan blog yang diambil daripada API JSON dan dipaparkan di halaman utama.
- Satu halaman bagi setiap catatan dengan imej tajuk selebar penuh.

## Tujuh langkah

| Langkah | Halaman | Anda akan belajar |
| --- | --- | --- |
| 1 | [Step-1-Template-and-Folders](Step-1-Template-and-Folders-ms) | Cara projek Flask memisahkan `templates` dan `static` |
| 2 | [Step-2-Home-Page](Step-2-Home-Page-ms) | Menghidangkan halaman daripada sebuah route |
| 3 | [Step-3-Static-Files](Step-3-Static-Files-ms) | `url_for('static', ...)` untuk CSS, JavaScript dan imej |
| 4 | [Step-4-Jinja-Include](Step-4-Jinja-Include-ms) | Berkongsi pengepala dan pengaki dengan `include` |
| 5 | [Step-5-About-and-Contact](Step-5-About-and-Contact-ms) | Lebih banyak route dan pautan yang dibina dengan `url_for` |
| 6 | [Step-6-Posts-from-API](Step-6-Posts-from-API-ms) | Membaca JSON daripada API dan membuat gelung dalam Jinja |
| 7 | [Step-7-Single-Post](Step-7-Single-Post-ms) | Route dengan bahagian berubah dan ralat 404 |

Mulakan dengan [Getting-Started](Getting-Started-ms) untuk menjalankan laman web ini sendiri.

## Gambaran keseluruhan projek

Kod ini mengikuti Clean Architecture yang ringan: `domain` (`Post`), `application` (kes guna `get_posts` dan `get_post`), `infrastructure` (membaca API) dan `presentation` (route Flask, templat dan fail statik). Semua pemalar terdapat dalam `src/blog/constants.py`. Flask ialah satu-satunya kebergantungan masa jalan.

[Repository](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/059-blog-capstone-part-2) · [Issue tracker](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/059-blog-capstone-part-2/issues)
