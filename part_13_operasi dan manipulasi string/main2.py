# mengubah case dari string
## mengubah menjadi huruf besar, kecil, kapital huruf pertama dll
salam = "bro!"
print("normal = " + salam)

# salam = salam.upper()
# print("upper = " + salam)

print(salam.upper())

# salam = salam.title()
# print("huruf awal kapital = " + salam)

print(salam.title())

salam = salam.lower()
print("lower = " + salam)

# pengecekan

salam = "sist"
print(salam + " is lower " + "= " + str(salam.islower()))
print(salam + " is upper " + "= " + str(salam.isupper()))
print(salam.istitle())

judul = "How To Win Friends And Influence People"
cek_judul = judul.istitle()
print(judul + " istitle = " + str(cek_judul))

cek_start = "thinking fast and slow"
print(cek_start)
print("starts with 'thi' = " + str(cek_start.startswith("thi")))

print("ends with 'slow' = " + str(cek_start.endswith("slow")) )

# penggabungan komponen join() dan split()

buah = ['apel', 'jeruk', 'anggur', 'kedondong']
print(buah)
gabung_buah = ' '.join(buah)
print(gabung_buah)

gabungan = "si anjing, katanya mau datang, tapi malah tidur"
print(gabungan)
pisah = gabungan.split(", ")
print(pisah)

# alokasi karakter rjust() ljust() center()

testes = "kucing"
alokasi = testes.rjust(20)
print('-' + alokasi + '-')

alokasi = testes.center(20,'.')
print('-' + alokasi + '-')

# strip, menghilangkan (kebalikannya)

alokasi = alokasi.strip('.') # menghilangkan tanda titik (.)
print(alokasi)


