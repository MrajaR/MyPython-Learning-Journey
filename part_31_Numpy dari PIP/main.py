### NUMPY
## sering digunakan untuk operasi matrix
import numpy as np


list_a = [1,2,3,4] # list biasa
vector_a = np.array([1,2,3,4 ]) # array numpy berupa vektor baris

print(f'list_a = {list_a}') # jika diprint muncul koma
print(f'vector_a = {vector_a}') # jika diprint akan muncul tanpa adanya koma

# print(list_a**2) <<tidak bisa dioperasikan secara matematis
print(vector_a**2) # dengan array kita bisa mengoperasikan angka_angka di dalamnya, akan mengkuadratkan setiap angka pada array
print(vector_a*5) # setiap bilangan dalam array dikalikan 5
# print(list_a*5) << tidak error tapi hasilnya malah list_a menjadi ada 2


## membuat matriks
matrix_b = np.array([(1,2),(3,4)])
print(f'\nmatrix b = \n{matrix_b}')
print(f'matrix b^2 = \n{matrix_b**2}')

# matriks dengan zero
zero_c = np.zeros((2,2)) # (2,2) adalah dimensinya
print(f'matriks zero c = \n{zero_c}')

# matriks dengan one
ones_d = np.ones((2,2)) # (2,2) adalah dimensinya
print(f'matriks ones d = \n{ones_d}')

# operasi matriks
jumlah = matrix_b + matrix_b**2 + ones_d
print(f'jumlah = \n{jumlah}')



















