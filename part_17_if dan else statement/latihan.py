print(20*"=")
print('Kalkulator Sederhana')
print(20*"=")

angka_1 = float(input('masukkan angka : '))
operator = input('pilih operator (*,/,+,-) : ')
angka_2 = float(input('masukkan angka : '))

if operator == '*' or operator == 'x':
    print(f'hasil = {angka_1*angka_2}')
elif operator == '/':
    print(f'hasil = {angka_1/angka_2}')
elif operator == '+':
    print(f'hasil = {angka_1+angka_2}')
elif operator == '-':
    print(f'hasil = {angka_1-angka_2}')
else:
    print('maaf tidak diketahui.')