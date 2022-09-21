## Assignment 2

Link hasil deploy dapat diakses (https://tugas2pbpjasmine.herokuapp.com/).

## Bagan

![Client](https://user-images.githubusercontent.com/103538319/190178780-0d4d5546-742e-4e0c-ae6d-311da1d0999d.jpg)

Setelah menerima request dari client, framework akan mencari `url` sesuai yang diminta, setelah menemukan `url` yang diminta maka `views` akan dipanggil. `views` akan mengquery data yang dengan models.py. lalu, `views` akan me-render berkas html yang sudah didefinisikan sesuai dengan data, dan hasilnya akan diberikan kepada client.

## Kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
venv adalah tools untuk membuat tools python yang terisolasi. Program yang berjalan di dalam venv memiliki modul-modulnya sendiri dan program dari luar tidak bisa mengaksesnya. Kita tetap bisa membuat aplikasi web berbasis Django tanpa menggunakan virtual environment hanya saja saat kita melakukan update packages dan dependencies seluruh data akan terubah secara global.

## Implementasi poin 1 - 4

### Poin 1(views.py)
Membuat fungsi bernama `show_katalog` untuk menerima parameter request serta membuat variabel yang dibutuhkan (nama dan npm). Fungsi pada views ini akan me-render katalog.html.
### Poin 2(urls.py)
Melakukan routing terhadap fungsi views yang telah dibuat, dengan menambahkan path baru untuk mengakses katalog. 
 ```
    ...
    path('katalog/', include('katalog.urls')),
    ...
 ```
 
### Poin 3(katalog.html)
Memasukkan data kedalam html menggunakan double curly brackets seperti berikut {{nama}}. Lalu menggunakan syntax for loop, untuk looping data-data dalam file models. 
```
{% for barang in list_barang %}
  <tr>
    <th>{{barang.item_name}}</th>
    <th>{{barang.item_price}}</th>
    <th>{{barang.item_stock}}</th>
    <th>{{barang.rating}}</th>
    <th>{{barang.description}}</th>
    <th>{{barang.item_url}}</th>
  </tr>
  {% endfor %}
 ```
### Poin 4(deploy)
memasukkan variable `HEROKU_APP_NAME` dan `HEROKU_API_KEY` pada github secret -> actions untuk mendeploy lalu run ulang workflow yang gagal.
