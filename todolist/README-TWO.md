# Tugas 6 PBP
## To Do List
📁 [Deployment](https://tugas2pbpjasmine.herokuapp.com/todolist/)

## Perbedaan antara asynchronous programming dengan synchronous programming
Asynchronous programming adalah teknik yang mengizinkan program untuk menjalankan program dan tetap bisa merespon hal lain bahkan saat  program dijalankan tanpa harus menunggu program selesai dibuat.
Synchronous programming adalah model programming dimana operasi berlangsung secara berurutan. Operasi terjadi satu persatu dimana program pindah ke langkah berikutnya ketika langkah saat ini telah menyelesaikan eksekusi dan telah mengembalikan hasil.

## Paradigma Event-Driven Programming
Event-driven programming adalah pendekatan di mana kode ditulis untuk menanggapi events. Peristiwa dapat dipicu oleh pengguna, seperti dengan mengklik ikon atau memasukkan beberapa teks.
Contoh penerapan:
```html
<button type="button" class="btn btn-outline-dark mx-auto d-block" data-bs-toggle="modal"
            data-bs-target="#exampleModal" style="text-align: center">Create new task</button>
```

## Penerapan asynchronous programming pada AJAX
penerapan asynchronous programming pada AJAX berguna untuk membuat konten web HTML yang responsif. Untuk mencapai tujuan ini mereka mempertahankan interaksi natural user dengan webpages. AJAX tidak bergantung pada web server, hal ini membuat sebuah _data-driven environment_ dibandingkan sebuah _page-driven environment_.

## Implementasi
1. Membuat view baru yang mengembalikan seluruh data task dalam bentuk JSON.
 ```py
        @login_required(login_url='/todolist/login/')
        def get_json(request):
            todolist = ToDoList.objects.filter(user=request.user)
            return HttpResponse(serializers.serialize("json", todolist), content_type="application/json")
```
   Menambahkan path JSON ke dalam `urlpatterns`
```py
        urlpatterns = [
            ...
            path('json/', get_json, name="get_json"),
            ...
        ]
```
2. Lakukan pengambilan task menggunakan AJAX GET.
3. Membuat tombol untuk membuat task baru yang membuka sebuah modal dengan form untuk menambahkan task
4. Membuat path `/todolist/add` yang mengarah ke view yang baru yang dibuat di urlpatterns
5. Menghubungkan form dengan path yang dibuat
6. Menutup modal setelah add task berhasil dilakukan, dan refresh webpage utama secara asinkronus


