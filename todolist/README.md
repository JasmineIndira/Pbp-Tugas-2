# Tugas 4 
## To Do List
📁 [Deployment](https://tugas2pbpjasmine.herokuapp.com/todolist/)

## Kegunaan {% csrf_token %} pada Elemen <form>

Django memiliki {% csrf_token %} untuk menghindari serangan seperti CRSF attack. {% csrf_token %} mengenerate token dari sisi server saat merender halaman dan mencross-check token jika ada request lain yang masuk. Jika request yang masuk tidak mengandung token, maka request itu tidak akan dieksekusi.
Jika pada elemen <form> tidak terdapat {% csrf_token %}, maka attacker bisa membuat request yang tidak diinginkan, karena request yang masuk tidak mengandung token untuk di cross-check agar tidak dilakukan eksekusi.

## Dapatkah membuat elemen <form> secara manual
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

