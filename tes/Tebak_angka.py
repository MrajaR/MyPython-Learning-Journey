# from math import exp

# user_input = input('masukkan angka : ')


# eulers = float(user_input[-3:])
# real_number = float(user_input[:-4])

# output = real_number * (10**eulers)

import os
import random

os.system('cls')

min_angka = 1
max_angka = 9

angka_rahasia = random.randint(min_angka, max_angka)


while True:
    print('*'*10 + 'SILAHKAN TEBAK ANGKA DARI 1-9' + '*'*10)
    user_input = int(input('Masukkan Tebakanmu : '))

    if user_input == angka_rahasia:
        print('tebakanmu berhasil\n')
        is_done = input('lanjut? (y/n) ')
        if is_done == 'n' or is_done == 'N':
            break
    elif user_input == (angka_rahasia - 1) and user_input < angka_rahasia:
        print('MENDEKATI BROO, GEDEIN DIKIT ANGKANYA!!\n')
    elif user_input == (angka_rahasia + 1) and user_input > angka_rahasia:
        print('MENDEKATI BROO, KURANGIN DIKIT ANGKANYA!!\n')
    else:
        print('salah bro, jauh')

print('UDAH DULU YAA MAIN TEBAK ANGKANYA, TERIMA KASIH :)')







