# contoh dengan list
angka = [0, 2, 3, 8, 9]
print(angka, '\n')

for i in angka:
    print('tes loop ') # jumlah perulangan sesuai dengan banyaknya item dalam list yakni 5 kali

for i in angka:
    print(f'i sekarang {i}') # i adalah item-item di dalam list yang ditampilkan secara berurutan

# contoh dengan range
print(5*'=', 'contoh dengan range', 5*'=')

angka_range = range(7) # range terdiri dari 7 angka, yakni 0,1,2,3,4,5,6
print(angka_range)

for i in angka_range:
    print('tes loop') # jumlah perulangan sesuai dengan banyaknya angka dalam range yakni 7 kali

for i in angka_range:
    print('i sekarang = ', i) # i adalah angka-angka dalam range yakni 0,1,2,3,4,5,6

print('==========')

# jika begini, maka print pertama dan kedua akan ditampilkan secara selang-seling sebanyak 4 kali (sesuai jumlah item dalam range)
for i in range(1,5): # range(1,5) artinya angka 1,2,3,4 secara berurutan
    print('tes loop')# jumlah perulangan sesuai dengan banyaknya angka dalam range yakni 4 kali
    print(f'i sekarang {i}') # i adalah angka-angka dalam range

# contoh dengan string
print(5*'=', 'contoh dengan string', 5*'=')

data_str = 'saya suka panco'

for i in data_str:
    print('tes loop')# jumlah perulangan sesuai dengan banyaknya karakter dalam string yakni 15 kali

for i in data_str:
    print(f"i sekarang {i}") # i adalah karakter-karakter string pada variabel data_str yang ditampilkan secara berurutan

# jika begini, maka print pertama dan kedua akan ditampilkan secara selang-seling sebanyak 15 kali
for i in data_str:
    print(f"i sekarang {i}") 
    print('tes loop')