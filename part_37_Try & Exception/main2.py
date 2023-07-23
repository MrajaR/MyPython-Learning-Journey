# contoh implementasi yang pertama
while(True):
    angka = int(input('masukkan angka : '))

    try:
        hasil = 10/angka
        print(f'hasil pembagian = {hasil}')
        is_done = input('apakah ingin lanjut (y/n)? ')
        if is_done == 'n' or is_done == 'N':
            break
    except ZeroDivisionError:
        print('pembagi nol, silahkan input angka lagi')

print('akhir dari program')

# 2. contoh implementasinya yang kedua
try:
    with open('part_37_Try & Exception/data.txt','r') as file:
        print(file.read())
except:
    print('file tidak ditemukan, membuat file data.txt baru')
    with open("part_37_Try & Exception/data.txt",'w',encoding='utf-8') as file:
        file.write('ini file baru')


# 3. CONTOH IMPLEMENTASI KETIGA, DENGAN MEMBUAT EXCEPTION SENDIRI
from numbers import Number

def tambah(a,b):
    if not isinstance(a, Number) or not isinstance(b, Number):
        raise 'INPUT HARUS ANGKA/INTEGER/FLOAT'
    return a+b

hasil = tambah(1,'2')
print(hasil)