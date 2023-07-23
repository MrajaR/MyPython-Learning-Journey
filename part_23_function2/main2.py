# Data = [10,5,15]

# Output = 0
# for x in Data:
#     Output += x

# '''
# 0+1
# 1+2
# 3+3
# 6+4
# 10+5
# 15+6
# 21+7
# 28+8
# 36+9
# 45+10

# sama dengan 55

# '''

# print(Output)

### function dengan *args

## ketika ingin memasukkan/menginput beberapa data ke dalam argument di function
## maka jumlah argumentnya harus sama dengan jumlah data yang diinput ke argument saat memanggil functionnya
def fungsi(nama,tinggi,berat): # 3 argument
    print(f'{nama} punya tinggi {tinggi} dan berat badan {berat}')

fungsi('sydmen',160, 65) # inputnya juga 3 argument

## cara yang lebih simple dan efisien
def fungsi_kedua(data_list): # satu argument saja
    data = data_list.copy()
    nama = data[0]
    tinggi = data[1]
    berat = data[2]
    print(f'{nama} punya tinggi {tinggi} dan berat badan {berat}')

# fungsi_kedua('markus',100,40) # tidak bisa karena melebihi jumlah argument yang ada pada fungsi_kedua, 
# harus menjadi list dahulu
fungsi_kedua(['markus',100,40]) # satu input ke dalam argument yakni berupa list

## cara yang jauh lebih baik, efisien dan simpel menggunakan *args (arguments)
def fungsi_ketiga(*args): # satu argument saja
    nama = args[0]
    tinggi = args[1]
    berat = args[2]
    print(f'{nama} punya tinggi {tinggi} dan berat badan {berat}')

fungsi_ketiga('charles', 182, 85) # dengan args kita bisa menginput banyak data ke dalam argument, walaupun argument di fungsi_ketiga terlihat cuma 1 yaitu *args

## studi kasus menggunakan *args
## *args bisa diganti dengan nama lain, misal *data

def tambah(*data:int) -> int:
    # argument data adalah tuple, sehingga iterable
    output = 0
    for x in data:
        output += x

    return output

output = tambah(1,2,3,4) # jumlah input untuk argumentnya bebas jika pake *args
print(output)

# cara baca loop di functionnya
'''
output += x
0+1 = 1
1+2 = 3
3+3 = 6
6+4 = 10

maka hasil loopnya, output = 10

'''

print(tambah(10,35,5))