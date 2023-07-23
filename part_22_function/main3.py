### function dengan default argument
## struktur:
## def nama_fungsi(argument = nilai defaultnya)
##     badan_fungsi


# contoh 1

def say_hello(nama = 'ganteng'): 
    '''function dengan default argument bisa dipanggil tanpa menginput argumentnya'''
    print(f'hallo {nama}')

## jika diprint tanpa argument, argumentnya akan berisikan nilai defaultnya yakni 'ganteng'
say_hello()

## bisa juga memanggil functionya dengan menginput argumentnya
## jika diinput/dipass nilai argumentnya, maka argument defaultnya akan tergantikan dengan yg diinput
say_hello('raja')

# contoh 2
def sapa_dia(nama, pesan = 'semoga hari-harimu menyenangkan'):
    '''function dengan argument tanpa nilai default dan dengan nilai default'''
    print(f'hai {nama}, {pesan}')

## akan error jika tidak diinput/dipass nilai dari argument 'nama'
# sapa_dia()

## menginput nilai untuk argument 'nama', dan argument 'pesan' akan berisikan nilai defaultnya
sapa_dia('sydmen') ## walaupun tidak dirincikan input 'sydmen' utk argument yg mana, tetap pasti akan terinput ke argument 'nama' karena argument 'nama' tidak ada nilai defaultnya

## menginput nilai untuk argument 'nama' dan 'pesan' secara berurutan
## bila argument argument 'pesan' diinput nilai baru, maka akan menimpa nilai defaultnya
sapa_dia('markus','jangan lupa bikin jembatan')

# contoh 3
## ini akan error karena non default argument hadir setelah default argument
# def hitung_pangkat(pangkat = 2, angka):
#     return angka**pangkat

def hitung_pangkat(angka, pangkat = 2):
    return angka**pangkat


## menginput nilai untuk argument 'angka', dan argument 'pangkat' akan berisikan nilai defaultnya yakni 2
print(hitung_pangkat(2))

## akan error, karena input posisional argument hadir setelah input beserta keyword argument
# print(hitung_pangkat(pangkat=3, 3))
# print(hitung_pangkat(angka=5, 2))

# yang benar
print(hitung_pangkat(4,3)) # jika penginputan argument tidak beserta keywordnya maka harus berurutan
print(hitung_pangkat(3, pangkat=3))
print(hitung_pangkat(angka = 2, pangkat=4))
print(hitung_pangkat(pangkat=3, angka = 5))


# contoh 4
## multi default argument 
def fungsi(input1 = 1, input2 = 2, input3 = 3, input4 = 4):
    return input1 + input2 + input3 + input4

# dapat merubah argument yang kita mau, dan yang tidak dirubah akan tetap default
hasil = fungsi(input3 = 10, input1 = 10 ) # penginputan argument jika di sertakan keywordnya tidak perlu berurutan
print(f'fungsinya = {hasil}')

    