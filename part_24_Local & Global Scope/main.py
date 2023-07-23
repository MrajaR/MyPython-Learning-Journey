### Global dan Local Scope dalam konteks function
## variabel global adalah variabel terluar yang dibuat tanpa adanya indentasi (tidak di dalam function)
## variabel global dapat diakses/dipanggil dimana saja (baik didalam function, loop , dan percabangan)
## variabel lokal adalah variabel di dalam function yang dibuat dengan indentasi
## variabel lokal hanya dapat diakses didalam scope local functionnya
## variabel lokal tidak dapat diakses diluar function

nama_global = 'sydmen' # ini adalah variabel global

# akses variabel global dalam function
def fungsi():
    print(f'fungsi untuk menampilkan {nama_global}') # memanggil variabel global di dalam function 

fungsi()

# akses variabel global dalam loop
for i in range(0,5):
    print(f'urutan ke {i} = {nama_global}') # memanggil variabel global di dalam loop 


# akses variabel global dalam conditional

if True:
    print(f'conditional statement menampilkan {nama_global}') # memanggil variabel global di dalam percabangan 

## Variabel Local Scope

def fungsi_2():
    nama_local = 'markus' # variabel local scope dalam function
    print(nama_local) # hanya bisa diakses/dipanggil dari dalam scope local function_2

# print(nama_local) # TIDAK BISA DIAKSES DARI LUAR FUNCTION, karena variabel nama_local adalah variabel local di dalam function_2 

## kasus 1 : penggunaan akses variabel
# variabel name di dalam function berikut tidak dibuat sebelum pemanggilannya
# tetapi masih dapat berfungsi/tidak eror jika di didefinisikan dibawahnya dengan variabel jenis global sebelum function dipanggil
def say_hello():
    print(f'halo. selamat siang {name}')

name = 'patur' # mendefinisikan variabel name yang dipanggil pada function di atas (jenis variabelnya global)
say_hello()
# name = 'patur' # error jika begini, karena pendefinisian dilakukan setelah function dipanggil

## kasus 2 : merubah variabel global
''' walaupun variable global dapat diakses didalam function, 
khusus untuk merubah variabel global maka harus diberi sintak global nama_variabel
yang berfungsi untuk mendapatkan izin akses untuk merubah variabel global tersebut'''
angka = 0
nama = 'iduy'

def ubah(angka_baru,nama_baru):
    global angka # artinya, mendapatkan izin akses untuk merubah variabel angka
    global nama # artinya, mendapatkan izin akses untuk merubah variabel nama
    angka = angka_baru
    nama = nama_baru

print(f'sebelum dirubah {angka,nama}')
ubah(6,'raja')
print(f'setelah dirubah {angka,nama}')

## contoh kasus 3 : di dalam for loop dan if statement

angka = 0

for i in range(0,5):
    angka += i
    print(angka)
    angka_dummy = 12 # tes membuat lokal variabel dalam for loop


print(f'\nangka dalam for loop = {angka} ')
print(f'angka dummy dalam for loop = {angka_dummy}') # masih dapat mengakses lokal variabel dalam for loop

if True:
    angka_dummy = 9 # membuat lokal variabel di dalam if statement
    angka = 0 # membuat lokal variabel di dalam if statement
 
print(f'angka dummy setelah dirubah dalam local scope if = {angka_dummy}') # dapat diakses
print(f'angka setelah dirubah dalam local scope if = {angka}') # dapat diakses


