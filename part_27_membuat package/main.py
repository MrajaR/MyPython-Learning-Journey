# package adalah folder yang berisikan module-module (modul adalah file .py yang berisikan banyak function yg siap dipnggil)
# package dan modul dibuat agar codingan menjadi rapih, readeble, dan efisien
# ketika pertama kali menjalankan package dan module makan akan muncul folder pycache
# folder pycache berisikan bitecode (sejenis bahasa mesin
# ) utk module-module yang kita pakai
# fungsi dari pycache agar waktu eksekusi code menjadi lebih cepat dan efisien

from sains import matematika,fisika

# from sains.fisika import energi_mekanik <-- hanya mengimport fungsi energi mekanik saja
# from sains.matematika import pangkat <-- hanya mengimport pangkat saja

hasil_tambah = matematika.kali(16,2)
print(hasil_tambah)

hasil_energi_mekanik = fisika.energi_mekanik(30,4)

print(f'energi mekanik = {hasil_energi_mekanik}')