# Tugas 4 
## To Do List
📁 [Deployment](https://tugas2pbpjasmine.herokuapp.com/todolist/)

## Kegunaan {% csrf_token %} pada Elemen <form>

Django memiliki {% csrf_token %} untuk menghindari serangan seperti CRSF attack. {% csrf_token %} mengenerate token dari sisi server saat merender halaman dan mencross-check token jika ada request lain yang masuk. Jika request yang masuk tidak mengandung token, maka request itu tidak akan dieksekusi.
Jika pada elemen <form> tidak terdapat {% csrf_token %}, maka attacker bisa membuat request yang tidak diinginkan, karena request yang masuk tidak mengandung token untuk di cross-check agar tidak dilakukan eksekusi.

## Dapatkah Membuat Elemen <form> Secara Manual
Elemen `<form>` dapat dibuat secara manual tanpa menggunakan `{{ form.as_table }}`. contohnya sebagai berikut
```
<form>
  <label for="fname">First name:</label><br>
  <input type="text" id="fname" name="fname"><br>
  <label for="lname">Last name:</label><br>
  <input type="text" id="lname" name="lname">
</form>
```

## Proses Alur Data dari Submisi yang Dilakukan oleh Pengguna Melalui HTML form, Penyimpanan Pata pada Database, Hingga Munculnya Data yang Telah Disimpan pada Template HTML

  a. Klik submit button
  b. Input diakses dengan memanfaatkan method `request.POST.get(name)` pada `views`, berikut potongan kodenya:
  
     ```
     if request.method == 'POST' and form.is_valid():
        title = form.cleaned_data['title']
        description = form.cleaned_data['description']
        task_baru = ToDoList.objects.create(title=title, description=description,
                                            user=request.user, date=datetime.date.today())
     ```
  
  c. Merender laman yang akan memuat data yang ingin ditampilkan, sehingga data pada HTML akan menampilkan versi terbaru.
  
## Implementasi
1. Menambahkan aplikasi baru pada tugas 2 django menggunakan `python manage.py startapp todolist` melalui terminal.
2. Menambahkan path `todolist` pada `urlspatterns` di `/project_django/urls.py`
   ```
    urlpatterns = [
    ...
    path('todolist/', include('todolist.urls')),
   ]
   ```
  Menambahkan `todolist` pada `INSTALLED_APPS` di `/project_django/settings.py`
   ```
    INSTALLED_APPS = [
    ...
    'todolist/',
   ]
   ```
3. Menambahkan model `ToDoList` pada `/todolist/models.py` berisi `user`, `date, `title`, dan `description` serta menentukan fields yang dipakai.
4. Membuat fungsi `show_todolist`, `register`, `login`, dan `logout` pada `todolist/views.py` dan kemudian membuat folder templates berisi template HTML untuk masing-masing fungsi yang dibuat
5. Menambahkan routing pada todolist pada `urls.py`.
  ```
  urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', add_todolist, name='add_todolist'),
    ...
  ]
  ```
6. Mendeploy ke Heroku dengan push berkas ke github dan merefresh workflow gagal di github.
  
## Internal CSS, Eksternal CSS, Inline CSS  
`Internal CSS` code diletakkan di dalam bagian <head> pada halaman. Class dan ID bisa digunakan untuk merujuk pada kode CSS, namun hanya akan aktif pada halaman tersebut. CSS internal diletakkan di dalam tag `<style>` `</style>`.
Manfaat internal CSS:
* Perubahan hanya terjadi pada 1 halaman
* Class dan ID bisa digunakan oleh internal stylesheet
* Tidak perlu meng-upload beberapa file karena HTML dan CSS bisa digunakan di file yang sama.

Kekurangan menggunakan Internal CSS:
* Meningkatkan waktu akses website
* Perubahan hanya terjadi pada 1 halaman – tidak efisien bila Anda ingin menggunakan CSS yang sama pada beberapa file.


`Eksternal CSS` adalah kode CSS yang ditulis terpisah dengan kode HTML Eksternal CSS ditulis di sebuah file khusus yang berekstensi .css. eksternal CSS biasanya diletakkan setelah bagian `<head>` `</head>`.

Manfaat External CSS
* Ukuran file HTML akan menjadi lebih kecil dan struktur dari kode HTML jadi lebih rapi.
* Loading website menjadi lebih cepat.
* File CSS dapat digunakan di beberapa halaman website sekaligus. 
Kekurangan External CSS
* Halaman akan menjadi berantakan, ketika file CSS gagal dipanggil oleh file HTML. Hal ini terjadi disebabkan karena koneksi internet yang lambat.

`Inline CSS` adalah kode CSS yang ditulis langsung pada atribut elemen HTML. Setiap elemen HTML memiliki atribut style, di situ lah inline CSS ditulis.
Manfaat Inline CSS
* Sangat membantu ketika Anda hanya ingin menguji dan melihat perubahan pada satu elemen.
* Berguna untuk memperbaiki kode dengan cepat.
* Proses permintaan HTTP yang lebih kecil dan proses load website akan lebih cepat.
Kekurangan Inline CSS
* Tidak efisien karena Inline style CSS hanya bisa diterapkan pada satu elemen HTML.

## Tag HTML5
  
## Tipe CSS Selector

1. `Type Selector`. Selektor ini akan memilih elemen berdasarkan nama tag.
```
p {
    color: blue;
}
```
```
<p>PBP Assignment 5</p>
```

2. `Selektor class`. selektor yang memilih elemen berdasarkan nama class yang diberikan.

```
.text-white {
    color: white;
}

.bg-teal {
    background: teal;
}
```
```
<h2 class="text-white bg-teal">Tutorial Lab 5</h2>
```

3. `Selektor ID` mirip dengan class tetapi hanya boleh digunakan oleh satu elemen saja.
```
#header {
    background: teal;
    color: white;
    height: 100px;
    padding: 50px;
}
```
```
<header id="header">
    <h1>Selamat Datang di Website Saya</h1>
</header>
```
4. `Selektor universal` adalah selektor yang digunakan untuk menyeleksi semua elemen pada jangkaua (scope) tertentu.
```
* {
    border: 1px solid grey;
}
```
  
## Cara Mengimplementasikan Checklist
  
Menggunakan framework Bootstrap untuk mengubah laman login, register, todolist, dan newtodolist. Pertama saya memasukkan link bootstrap pada `base.html`
```
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet"
integrity="sha384-iYQeCzEYFbKjA/T2uDLTpkwGzCiq6soy8tYaI1GyVh/UjpbCx/TYkiZhlZB6+fzT" crossorigin="anonymous">
```
Kemudian saya mengkostumisasi elemen-elemen dalam HTML yang sudah saya buat sebelumnya.
Melakukan kostumisasi pada laman todolist dengan membuat 1 card untuk setiap task yang ditambahkan.
Membuat keempat halaman menjadi responsive.
Melakukan deploy pada Heroku.



