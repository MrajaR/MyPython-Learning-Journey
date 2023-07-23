# membuat alias dengan sintaks 'as', nama aliasnya bebas semau kita
from matematika import tambah as t
from matematika import kali as k
from matematika import pangkat as namanya_terserah_asliDah

import matematika as kntl # <-- dapat dilakukan juga

hasil_tambah = t(1,3,5) # <-- tidak usah lagi menggunakan namespace matematika jika menggunakan sintaks from ketika import
print(f'hasil tambah = {hasil_tambah}')

hasil_kali = k(1,3,5) # <-- tidak usah lagi menggunakan namespace matematika jika menggunakan sintaks from ketika import
print(f'hasil kali = {hasil_kali}')

pangkat3 = namanya_terserah_asliDah(3) # <-- tidak usah lagi menggunakan namespace matematika jika menggunakan sintaks from ketika import
print(f'hasil pangkat 3 dari 9 = {pangkat3(9)}')

hasil_tambah2 = kntl.tambah(4,5,1)
print(f'hasil tambah kedua {hasil_tambah2}')