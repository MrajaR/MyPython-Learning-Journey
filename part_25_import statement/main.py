### import statement

## fungsinya adalah untuk mengambil program dari file external.py

# 1.UNTUK MENYAMBUNG PROGRAM DARI FILE EXTERNAL EKSTENSI .PY

import program_print # baris code yang ada di file program_print.py diimport disini dan akan jalan disini
import program_syd

# 2. IMPORT DENGAN DATA
# file variabel dan variabel_2 sama" memiliki variabel yang sama yakni nama
# oleh karenanya memang dibutuhkan penulisan namespacenya sebelum variabel
import variabel 
import variabel_2

# untuk mengakses variabel nama diperlukan penyebutan nama 
# print(nama) <-- eror tidak bisa di python, harus ada namespace, toh pun andaikata bisa, ingin print variabel nama dari file mana?
print(variabel.nama) # <-- variabel nama ada di namespace variabel
print(variabel_2.nama) # <-- variabel nama ada di namespace variabel_2

# 3. IMPORT FILE EXTERNAL BERISI FUNCTION

import matematika

# untuk mengakses functionnya diperlukan keterangan namespace di depan functionnya
hasil = matematika.luas_segitiga(6,4)
print(hasil)