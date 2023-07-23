# Latihan 

# sisi = int(input('silahkan hitung = '))

# # menggunakan for
# # dummy variable
# count = 1

# for i in range(sisi):
#     print('*'*count)
#     count += 1

# count = 1
# sisi = int(input('silahkan hitung = '))

# while True:
#     tes = '*'*count
#     print(tes)
#     count += 1

#     if len(tes) == sisi:
#         break

# hanya ganjil saja

while True:
    angka = int(input('masukkan angka = '))

    hasil = angka//2 # hasil dari floor division adalah pembagi yang menghasilkan hasil terdekat

    print(f'hasil floow division dengan 2 = {hasil}')

    isdone = input('apakah lanjut ? (y/n)')

    if isdone == 'y':
        continue

    else:
        break



sisi = 10
count = 1

while True:
    if count%2: # jika jumlah '*' ganjil
        print('*'*count)
        count += 1
    else: # jika jumlah '*' genap
        count += 1
        continue
        
    if count > sisi:
        break

print('akhir dari while \n')

# segitiga sama kaki

sisi = 19
count = 1
spasi = sisi // 2

while True:
    if count%2:
        print(' '*spasi,'+'*count)
        count += 1
        spasi -= 1
    else:
        count += 1
        continue

    if count > sisi:
        break




