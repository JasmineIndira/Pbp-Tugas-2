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


