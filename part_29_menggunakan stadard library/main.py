import datetime # didalam modul datetime sendiri terdapat import statement utk modul lain

# cara untuk menampilkan waktu sekarang
#                modulnya|classnya|functionnya
waktu_sekarang = datetime.datetime.now() # function now() ada di dalam class datetime

print(f'waktu dan tanggal sekarang : {waktu_sekarang}')

tahun = waktu_sekarang.year

print(f'tahun = {tahun}')

tanggal = waktu_sekarang.strftime('%A')

print(f'hari = {tanggal}')

from collections import Counter


# menghitung jumlah item/data akan ribet jika manual, seperti berikut:
data_a = ["a","a","b","c","a","b","c","a","b","b","d"]

jumlah = 0

for i in data_a:
    if i == "a":
        jumlah += 1

print(f'jumlah huruf a = {jumlah}')

# jika menggunakan class counter dari modul collection maka akan lebih simpel, seperti berikut:

jumlahDenganCounter = Counter(data_a)

print(jumlahDenganCounter) # <-- hasilnya berupa dict, dengan keynya adalah item yang ada di list data_a dan valuenya adalah jumlah dari masing" item
print(f"jumlah a dihitung dengan counter = {jumlahDenganCounter['a']}")

# library untuk membaca file
import io

file = io.open("part_29_menggunakan stadard library\puisi_text.txt","r")
print(file.read())
