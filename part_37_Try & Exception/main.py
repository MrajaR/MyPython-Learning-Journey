## 1. EXCEPTION KARENA ANGKA TIDAK BISA DIBAGI 0
print(f"{'EXCEPTION ZERO DIVISION ERROR':^30}")
input_user = int(input('masukkan angka : '))
hasil = None # dummy

try: # normalnya akan mencoba block try
    hasil = 10/input_user
except Exception as e: # jika block try tidak bisa dipenuhi dan error, maka akan pindah ke except, dan di syntax ini akan menangkap exception secara umum
    print(f"terjadi exception : {type(e)}") # type(e) berguna untuk mengetahui nama/tipe exception

print(hasil)

# BISA JUGA BEGINI
input_user = int(input('masukkan angka : '))
hasil = None # dummy

try: # normalnya akan mencoba block try
    hasil = 10/input_user
except: # jika block try tidak bisa dipenuhi dan error, maka akan pindah ke except, dan di syntax ini akan menangkap exception secara umum
    print("terjadi exception karena pembagi 0") 

print(hasil)

# BISA JUGA BEGINI
input_user = int(input('masukkan angka : '))
hasil = None # dummy

try: # normalnya akan mencoba block try
    hasil = 10/input_user
except ZeroDivisionError: # jika block try tidak bisa dipenuhi dan error, maka akan pindah ke except, dan di syntax ini hanya akan menangkap exception khusus utk exception tipe zerodivision error
    print("terjadi exception karena pembagi 0") 

print(hasil)

## 2. EXCEPTION KARENA STRING TIDAK DI CAST KE INT
print(f"{'EXCEPTION TYPE ERROR':^30}")
input_user = (input('masukkan angka : ')) # tidak dicasting ke int
hasil = None # dummy

try: # normalnya akan mencoba block try
    hasil = 10/input_user
except Exception as e: # jika block try tidak bisa dipenuhi dan error, maka akan pindah ke except, dan di syntax ini akan menangkap exception secara umum
    print(f"terjadi exception: {type(e)}") # type(e) berguna untuk mengetahui nama/tipe exception

print(hasil)

# bisa juga begini
input_user = (input('masukkan angka : '))
hasil = None # dummy

try: # normalnya akan mencoba block try
    hasil = 10/input_user
except: # jika block try tidak bisa dipenuhi dan error, maka akan pindah ke except, dan di syntax ini akan menangkap exception secara umum
    print("terjadi exception karena int dibagi string") # type(e) berguna untuk mengetahui nama/tipe exception

print(hasil)

# BISA JUGA BEGINI
input_user = (input('masukkan angka : '))
hasil = None # dummy

try: # normalnya akan mencoba block try
    hasil = 10/input_user
except TypeError: # jika block try tidak bisa dipenuhi dan error, maka akan pindah ke except, dan di syntax ini hanya akan menangkap exception bertipe typeerror
    print("terjadi exception karena int dibagi string") # type(e) berguna untuk mengetahui nama/tipe exception

print(hasil)