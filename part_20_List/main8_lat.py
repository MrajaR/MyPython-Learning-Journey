# program list buku

list_buku = []

while True:
    print("\nMasukkan data buku")
    judul = input("Judul Buku : ")
    penulis = input('Masukkan Nama Penulis : ')

    buku_baru = [judul,penulis]
    list_buku.append(buku_baru)

    print('\n ', '='*10)
    
    for index,buku in enumerate(list_buku):
        print(f'{index+1}. judul = {buku[0]}, penulis = {buku[1]}')

    respon_user = input('\napakah ingin lanjut?, (y/n) ')

    if respon_user == 'n':
        break
    if respon_user == 'y':
        continue

print('\nhasil:')
for index,buku in enumerate(list_buku):
    print(f'{index+1} | judul : {buku[0]} | penulis {buku[1]}')

print('\nPROGRAM SELESAI')
# print(list_buku)