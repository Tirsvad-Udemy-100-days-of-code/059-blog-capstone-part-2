[English](Getting-Started) · [Dansk](Getting-Started-da) · **Bahasa Malaysia**

# Bermula

## Keperluan

- Python 3.13 atau lebih baharu
- Git
- Doxygen (pilihan, hanya untuk dokumentasi API)

## Cipta dan gunakan persekitaran maya tempatan

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Pada Linux dan macOS gunakan `python3 -m venv .venv` dan `source .venv/bin/activate`. Keluar daripada persekitaran dengan `deactivate`.

## Jalankan laman web

```bash
python -m blog.main
```

Buka <http://127.0.0.1:5000>. Catatan diambil daripada endpoint dalam `src/blog/constants.py`; jika endpoint tidak dapat dicapai, salinan yang disertakan dalam pakej akan digunakan.

## Jalankan ujian

```bash
python -m pytest
```

Ujian tidak pernah menggunakan rangkaian. Bina dokumentasi kod dengan `doxygen Doxyfile`.

## Apa yang kita pelajari

- Persediaan yang boleh diulang: persekitaran maya, `pip` dinaik taraf, projek dipasang dalam mod boleh sunting.
- Satu arahan untuk menjalankan laman web dan satu untuk menjalankan ujian, kedua-duanya ditulis dalam README.
