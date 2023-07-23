"""latihan fungsi"""

import os

os.system('cls')

def persegi_panjang():
    print('\nMENGHITUNG LUAS PERSEGI PANJANG')
    panjang = int(input('masukkan panjang (cm) :'))
    lebar = int(input('masukkan lebar (cm) :'))
    hasil = f'luas persegi panjang = {panjang*lebar} cm persegi'
    return hasil

def segitiga():
    print('\nMENGHITUNG LUAS SEGITIGA')
    alas = int(input("masukkan alas segitiga (cm): "))
    tinggi = int(input('masukkan tinggi segitiga (cm): '))
    hasil = f'luas segitiga = {(1/2)*alas*tinggi} cm persegi'
    return hasil

while True:
    print(f"\n{'---PROGRAM MENGHITUNG LUAS BANGUN DATAR---':^50}\n")
    print('1. program menghitung luas segitiga\n2. program menghitung luas persegi panjang')
    input_user = input('silahkan pilih (1 atau 2) : ')

    if input_user == '1':
        print(segitiga())

    if input_user == '2':
        print(persegi_panjang())

    Is_done = input('\napakah ingin lanjut? (y/n) ')

    if Is_done == 'y':
        continue
    if Is_done == 'n':
        break

print('\nTERIMA KASIH TELAH MENGGUNAKAN PROGRAM INI')