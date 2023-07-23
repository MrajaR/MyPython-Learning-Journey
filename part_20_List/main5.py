## nested list

data_0 = [1,2]
data_1 = [3,4,7]

data_list_biasa = [1,2,3,4]

print(f'ini adalah list biasa = {data_list_biasa}')

list_2d = [data_0, data_1, 2, 3.9]
print(f'ini adalah list 2d = {list_2d}')

# contoh penggunaan

peserta_0 = ['sydmen', 23, "laki-laki"]
peserta_1 = ['dukun', 21, 'laki-laki']
peserta_2 = ['markus', 18, 'laki-laki']

list_peserta = [peserta_0, peserta_1, peserta_2]
print(f'\npeserta = {list_peserta}\n')


for peserta in list_peserta: # artinya, untuk setiap item-item pada list peserta secara berurutan (dimulai dari peserta_0, lalu peserta_1, dan trakhir peserta_2 lakukan hal berikut
    print(f'nama = {peserta[0]}') # 3 baris statement ini akan diterapkan untuk tiap-tiap item pada list_peserta secara berurutan, dimulai dari yang paling awal dulu yakni peserta_0
    print(f'umur = {peserta[1]}') # 3 baris statement ini akan diterapkan untuk tiap-tiap item pada list_peserta secara berurutan, dimulai dari yang paling awal dulu yakni peserta_0
    print(f'kelamin = {peserta[2]}\n') # 3 baris statement ini akan diterapkan untuk tiap-tiap item pada list_peserta secara berurutan, dimulai dari yang paling awal dulu yakni peserta_0

for peserta in list_peserta:
    print(peserta)

# problem dengan reference

list_copy = list_peserta.copy() # menduplikat nested list list_peserta
print(f'\ncopy list dari list peserta = \n{list_copy}')
peserta_0[0] = 'ilham' # merubah variabel berisi list yang menjadi reference yg sama bagi list_peserta dan list_copy
print(f'copy list dari list peserta = \n{list_copy}') # alhasil walaupun sudah diduplikasi tetap saja duplikatnya berubah karena masih 1 reference yakni dengan variabel peserta_0, peserta_1, peserta_2, isi item variabel peserta_0, peserta_1, peserta_2 tidak ikut diduplikasi
print(f'peserta = {list_peserta}\n')

# kasus lain dengan reference
a = 1 # jika variabel-variabel ini dirubah nilainya, maka akan merubah list_tes dan list duplikatnya, karena ini adalah reference bagi list_tes dan duplikatnya
b = 'markus' # jika variabel-variabel ini dirubah nilainya, maka akan merubah list_tes dan list duplikatnya
c = '18' # jika variabel-variabel ini dirubah nilainya, maka akan merubah list_tes dan list duplikatnya

list_tes = [a, b, c]
print(list_tes)

list_copytes = list_tes.copy() # duplikasi list_tes
print(f'\n{list_copytes}\n')

list_tes[0] = 2 # merubah index ke 0 dari list_tes
print(list_tes)
print(f'{list_copytes}\n') # list_copytes yg merupakan duplikat tidak terpengaruhi dgn perubahan di index ke-0 di list tes 

b = 'aris' # merubah variabel berisi string tunggal yang menjadi reference bagi list_tes (tidak bisa merubah sperti ini kcuali merubah data pada list)
print(list_tes) # tidak berubah
print(f'{list_copytes}\n') # tidak berubah