import datetime
import os
import time
import random
import string

# template dictionary yang kemudian akan digunakan keynya di dictionary baru di bawah
mahasiswa_template = {
    "Nama":'mahasiswa',
    'NIM':'000',
    'SKS_lulus':0,
    'Lahir': datetime.datetime(1111,11,1)
}

Data_Mahasiswa = {}

os.system('cls') # menghilangkan keterangan directory di terminal
print(f"{'SELAMAT DATANG':^20}")
print(f"{'DATA MAHASISWA':^20}")
print('-'*20)

while True:
    tampungan = dict.fromkeys(mahasiswa_template.keys()) # membuat dictionary baru dengan method dict(), dan mengambil key dari dict mahasiswa_template untuk dijadikan key dalam dict baru menggunakan method fromkeys()
    print(tampungan)
    # mengassign input-input dari user sebagai value untuk masing" key dari dict mahasiswa
    tampungan['Nama']= input('Nama Mahasiswa: ')
    tampungan['NIM']= input('Masukkan NIM:')
    tampungan['SKS_lulus']= int(input('Masukkan SKS: '))
    TAHUN = int(input('Tahun lahir: '))
    BULAN = int(input('Bulan lahir: '))
    TANGGAL = int(input('Tanggal lahir: '))
    tampungan['Lahir']= datetime.datetime(TAHUN,BULAN,TANGGAL)
    print(tampungan)

    time.sleep(3)

    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
    Data_Mahasiswa.update({KEY:tampungan})
    print(f'\n{Data_Mahasiswa}\n')

    time.sleep(3)

    print(f"{'KEY':<8} {'Nama':^17} {'NIM':^10} {'SKS':^10} {'Lahir':^10}")
    print('-'*60)

    for mahasiswa in Data_Mahasiswa:
        KEY = mahasiswa
        NAMA = Data_Mahasiswa[mahasiswa]['Nama']
        NIM = Data_Mahasiswa[mahasiswa]['NIM']
        SKS = Data_Mahasiswa[mahasiswa]['SKS_lulus']
        LAHIR = Data_Mahasiswa[mahasiswa]['Lahir'].strftime('%x')

        print(f'{KEY:<8} {NAMA:^17} {NIM:^10} {SKS:^10} {LAHIR:^10}')

    lanjut_or_not = input('\napakah anda ingin lanjut? y/n ')

    if lanjut_or_not == 'n':
            break
    if lanjut_or_not == 'y':
            continue

print(f'\ntes = {tampungan}') # bisa dipanggil di luar loop (padahal dibaut didalam loop), alasan kenapa dict ini ke reset di loop di atas karena adanya penggunaan method dict.fromkeys() setiap kali loop
print('\nTHE END OF THE PROGRAM')        
    
