from matematika import tambah, kali, pangkat # memilih untuk hanya mengimport beberapa function dari module matematika
# from matematika import * <-- artinya mengimport semua function dalam module matematika

hasil_tambah = tambah(1,3,5) # <-- tidak usah lagi menggunakan namespace matematika jika menggunakan sintaks from ketika import
print(f'hasil tambah = {hasil_tambah}')

hasil_kali = kali(1,3,5) # <-- tidak usah lagi menggunakan namespace matematika jika menggunakan sintaks from ketika import
print(f'hasil kali = {hasil_kali}')

pangkat3 = pangkat(3) # <-- tidak usah lagi menggunakan namespace matematika jika menggunakan sintaks from ketika import
print(f'hasil pangkat 3 dari 9 = {pangkat3(9)}')