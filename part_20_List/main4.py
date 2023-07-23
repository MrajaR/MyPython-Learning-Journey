## teknik duplikasi/copy list

a = ['Ucup','Otong','Dudung']
print(f'a = {a}')

b = a # ini pass by reference, jika duplikasi dilakukan seperti ini maka perubahan yang kita terapkan pada salah satu list juga akan berdampak yang sama pada list yang lain
print(f'a = {a}')

a[1] = 'Michael' # merubah index 1 pada list a menjadi 'Michael' juga akan merubah index 1 pada list b dengan 'Michael' juga
b.sort() # menyortir list b juga akan menyortir list
print(f'a = {a}')
print(f'b = {b}')

# address yang sama dari kedua list
print(f'address a = {hex(id(a))}')
print(f'address b = {hex(id(b))}')

# cara yang duplikasi list yang benar dan baik adalah dengan menggunakan method copy()
a = ['dante', 'sydmen', 'ibnu', 'markus']
print(f'\nlist a = {a}')

b = a.copy()

print(f'list b dari duplikat a = \n{b}')

# addressnya pun skrg sudah berbeda
print(f'\naddress a = {hex(id(a))}')
print(f'address b = {hex(id(b))}')

# pembuktian
b.sort()
print(f'\nhasil sortir list b tidak akan merubah list a = \n{b}')
print(f'sementara ini list a, tetap sama seperti di awal = \n{a}')