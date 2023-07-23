# pass
angka = 0

while angka < 5:
    angka += 1

    if angka == 3:
        pass # dummy, hanya menandakan jika suatu baris code tidak diimplementasikan (terutama di fungsi atau class oop)

    print(angka)

# continue
angka = 0

while angka < 5:

    angka += 1
    print(f'angka sekarang {angka}')
    
    if angka == 3:
        print(f'angka spesial = {angka}')
        continue # akan membuat loop skip aksi dibawahnya dan lompat ke awal loop dari atas
    
    print('whatsupp')





