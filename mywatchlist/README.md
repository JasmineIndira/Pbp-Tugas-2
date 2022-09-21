# Tugas 3
## My Watchlist
📁[Deployment](https://tugas2pbpjasmine.herokuapp.com/mywatchlist/)

## Perbedaan Antara JSON, XML, dan HTML

JSON adalah data intercharge ringan yang digunakan untuk mengirim data antar komputer. JSON hanya menyediakan sepsifikasi data encoding. JSON lebih terkenal daripada XML karena JavaScript lebih banyak digunakan sekarang.

XML adalah bahasa yang mengspesifikasi custom markup languages, dan menyediakan lebih banyak dari data intercharge. XML memiliki standar yang membingungkan dan tidak se efisien JSON. 

HTML  adalah bahasa markup standar yang digunakan untuk membuat halaman website dan aplikasi web. HTML menggunakan struktur kode tag dan attribute untuk mark up halaman website.

## Mengapa Data Delivery Penting dalam Pengimplementasian Sebuah Platform?
Data Delivery Penting dalam Pengimplementasian Sebuah Platform agar user/client bisa melakukan CRUD process (Create, Read, Update, Delete).  Untuk melakukannya diperlukan data delivery format seperti JSON, XML, dan juga HTML.

## Implementasi
1. Menambahkan aplikasi baru pada tugas 2 django menggunakan `python manage.py startapp mywatchlist` melalui terminal. 
2. Menambahkan path `mywatchlist` pada `urlspatterns` di `/project_django/urls.py`
   ```
    urlpatterns = [
    ...
    path('mywatchlist/', include('mywatchlist.urls')),
   ]
   ```
  Menambahkan `mywatchlist` pada `INSTALLED_APPS` di `/project_django/settings.py`
 ```
    INSTALLED_APPS = [
    ...
    'mywatchlist/',
   ]
 ```
3. Menambahkan model `MyWatchList` pada `/mywatchlist/models.py` berisi `watched`, `title`, `rating`, `release date`, dan `review` serta menentukan fields yang dipakai.
4. Membuat folder baru `fixtures` berisi 10 data film yang akan dimasukkan ke database.
5. Mengimplementasi fitur untuk menyajikan data dalam format `html`, `xml`, dan `json` di `mywatchlist/views.py` serta melakukan routing.
6. Membuat unit tes pada `tests.py`
7. Menambahkan `python manage.py loaddata movie_catalog_data.json` pada procfile.
8. Mendeploy ke Heroku dengan push berkas ke github dan merefresh workflow gagal di github.

## Akses URL menggunakan postman
####1. html
![html](https://user-images.githubusercontent.com/103538319/191543921-f85db1e9-177d-4c2e-ab7d-6568735e2975.jpg)
####2. xml
![xml](https://user-images.githubusercontent.com/103538319/191544246-db1b6f9e-31f9-4dd6-a326-4b411cbe9286.jpg)
####3. json
![json](https://user-images.githubusercontent.com/103538319/191544546-5fb47fbb-8f6b-41d8-912d-16a51f8d8446.jpg)

