"""
untuk method yang berfungsi untuk merubah-rubah list (seperti pop,remove,append,insert,extend, dll)
tidak bisa langsung ditampilkan didalam print(), mesti di declare dulu diatasnya/masukkan dalam variabel diatasnya
baru bisa diprint (print variabel yang menampung methodnya atau print listnya)
akan tetapi method yang hanya digunakan untuk mencari tau informasi
tentang list (seperti index,len,count. dll) bisa langsung dimasukkan dalam print()
sebagai contoh : print(len(list_name))
"""

data_angka = [1,2,2,2,3,6,4,6,3,7,9,2,7,1,1,1,1,1,1,0]

print(f'list data angka = {data_angka}')

# count data

jumlah_angka_1 = data_angka.count(1) # bisa langsung diprint tanpa dimasukkan ke variable
print(f'jumlah angka 1 pada data angka = {jumlah_angka_1}')
print(data_angka.count(1)) # bisa langsung diprint tanpa dimasukkan ke variable

# ambil posisi/index item

data = ['dante', 'sydmen', 'ibnu', 'markus']
print(f'\ndata = {data}')
print(data.index('dante'))

# menyortir list/ mengurutkan list

data.sort(reverse=True) # reverse bisa jadi parameter (tambah value True)
print(data)
data_angka.sort()
print(data_angka)
data_angka.reverse()# reverse bisa juga jadi method
print(data_angka)