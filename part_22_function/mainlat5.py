'''LATIHAN NGIKUTIN KELAS TERBUKA'''
import os

os.system('cls')

def header():
    print(f"\n{'--PROGRAM MENGHITUNG LUAS DAN KELILING LINGKARAN--':^50}\n")
    print('Pilih Program:\n1. Menghitung Luas Lingkaran\n2. Menghitung Keliling Lingkaran\n')

def input_user():
    jari_jari = float(input('Masukkan panjang jari-jari : '))
    return jari_jari

def hitung_luas(jari_jari):
    return 3.14 * (jari_jari**2)

def hitung_keliling(jari_jari):
    return 2 * 3.14 * jari_jari

def display(massage, value):
    print(f'hasil perhitungan {massage} = {value}')

while True:
    header()
    opsi = input('Pilih Program (1 atau 2) : ')
    
    JARI_JARI = input_user()
    LUAS = hitung_luas(JARI_JARI)
    KELILING = hitung_keliling(JARI_JARI)
    
    if opsi == '1':
        # print(f'Luas lingkaran = {hitung_luas(JARI_JARI)}')
        display('luas', LUAS)

    if opsi == '2':
        # print(f'Keliling lingkaran = {hitung_keliling(JARI_JARI)}')
        display('keliling', KELILING)

    is_done = input('\napakah ingin lanjut? (y/n) ')

    if is_done == 'n':
        break

print('\nTERIMA KASIH TELAH MENGGUNAKAN PROGRAM INI')

