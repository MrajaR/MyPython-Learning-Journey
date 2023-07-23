# a = 10, a adalah variabel dengan nilai 10

# tipe data : angka satuan/bilangan bulat (integer)
data_integer = 1 # 1 adalah integer
print("data_integer valuenya : ", data_integer)
print("data_integer ini bertipe :", type(data_integer))

# tipe data : angka dengan koma (float)
data_float = 1.5
print("data : ", data_float)
print("- data ini bertipe :", type(data_float))

# tipe data : kumpulan karakter yang diapit tanda petik 2 atau petik 1 (float)
data_string = "ini adalah string"
print("data : ", data_string)
print("- data ini bertipe :", type(data_string))

# tipe data : binary true/false (boolean)
data_bool = True
print("data : ", data_bool)
print("- data ini bertipe :", type(data_bool))

## tipe data khusus

# bilangan kompleks (complex)
data_complex = complex(5,6)
print("data : ", data_complex)
print("- data ini bertipe :", type(data_complex))

# tipe data dari bahasa C

from ctypes import c_double

data_c_double = c_double(10.5)
print("data : ", data_c_double)
print("- data ini bertipe :", type(data_c_double))