# Tugas 4 
## To Do List
📁 [Deployment]

## Kegunaan {% csrf_token %} pada Elemen <form>

Django memiliki {% csrf_token %} untuk menghindari serangan seperti CRSF attack. {% csrf_token %} mengenerate token dari sisi server saat merender halaman dan mencross-check token jika ada request lain yang masuk. Jika request yang masuk tidak mengandung token, maka request itu tidak akan dieksekusi.
Jika pada elemen <form> tidak terdapat {% csrf_token %}, maka attacker bisa membuat request yang tidak diinginkan, karena request yang masuk tidak mengandung token untuk di cross-check agar tidak dilakukan eksekusi.

## Dapatkah membuat elemen <form> secara manual
