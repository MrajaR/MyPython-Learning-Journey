# break

angka = 0

while angka < 7:
    angka += 1
    print(f'angka sekarang {angka}')

    if angka == 4:
        print(f'sudah mendapatkan angka = {angka}')
        break # akan memutus loop/mengakhiri loop

    print('nice!!')

angka = 0

data_user = int(input('hitung sampai = '))

while True:
    angka += 1
    print(f'hitung = {angka}')

    if angka == data_user:
        break # akan memutus loop/mengakhiri loop