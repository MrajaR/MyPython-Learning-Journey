# casting tipe data adalah merubah satu tipe data ke tipe data lain
# tipe data = int, float, str, bool

# casting data type dari integer
print("=========INTEGER=========")
data_int = 1
print("data = ", data_int, ",type = ", type(data_int))

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int) # akan false jika nilai int = 0
print("data = ", data_float, ",type =", type(data_float))
print("data = ", data_str, ",type =", type(data_str))
print("data = ", data_bool, ",type =", type(data_bool))


# casting data type dari float
print("=========FLOAT=========")
data_float = 9.5
print("data = ", data_float, ",type = ", type(data_float))

data_int = int(data_float) # data integer akan dibulatkan ke bawah
data_str = str(data_float)
data_bool = bool(data_float) # akan false jika nilai float = 0
print("data = ", data_int, ",type =", type(data_int))
print("data = ", data_str, ",type =", type(data_str))
print("data = ", data_bool, ",type =", type(data_bool))

# casting data type dari boolean
print("=========BOOLEAN=========")
data_bool = True #jika true maka int dan floatnya menjadi 1, jika false maka menjadi 0
print("data = ", data_bool, ",type =", type(data_bool))

data_int = int(data_bool)
data_str = str(data_bool)
data_float = float(data_bool)
print("data = ", data_int, ",type =", type(data_int))
print("data = ", data_str, ",type =", type(data_str))
print("data = ", data_float, ",type =", type(data_float))

# casting data type dari string
print("========STRING========")
data_str = "bgi" # tidak bisa dicasting ke tipe data lain (error) apabila string bernilai huruf (harus berisi angka)
print("data = ", data_str, ",type =", type(data_str))

# data_int = int(data_str)
# data_float = float(data_str)
data_bool = bool(data_str) 
print("data = ", data_int, ",type =", type(data_int))
print("data = ", data_float, ",type =", type(data_float))
print("data = ", data_bool, ",type =", type(data_bool))

"""khusus untuk casting string ke boolean,
semua value dalam string yang dicasting ke boolean akan bernilai true,
tetapi jika stringnya kosong/tidak diisi maka booleannya akan bernilai false"""

