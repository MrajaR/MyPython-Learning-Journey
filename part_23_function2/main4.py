### lambda function

def f_kuadrat(angka):
    '''fungsi biasa'''
    return angka**2

print(f'hasil dari fungsi kuadrat biasa= {f_kuadrat(3)}')

## penggunaan lambda function
## output = lambda argument: expression
## output adalah nama fungsinya
## lambda otomatis mempunyai return
kuadrat_lambda = lambda angka:angka**2

print(f'hasil dari fungsi kuadrat lambda = {kuadrat_lambda(5)}')

pangkat = lambda num,pow:num**pow

print(f'hasil dari lambda function pangkat = {pangkat(2,3)}')

## kegunaan lambda function
## sorting utk list

data_list = ["aurelius",'syd','megalodon','raja','markus']

data_list.sort()
print(f'sorted list = {data_list}')

# data_list.sort(key=len)
# print(f'sorted list by len = {data_list}')

def panjang_nama(nama):
    return len(nama)

data_list.sort(key=panjang_nama) # perhatikan, function panjang_nama dipanggil tanpa input argument. dikarenakan menjadi value bagi key dan otomatis argument akan diisi dengan tiap-tiap item pada list data_list

print(f'sorted list by len using function = \n{data_list}')

print(data_list)
data_list = ["aurelius",'syd','sabronlodon','raja','markus']

print(f'reset data_list = {data_list}')

## sort by len menggunakan lambda
data_list.sort(key = lambda x:len(x))
print(f'sorted by len dengan lambda = \n {data_list}')

## filter list menggunakan lambda
data_angka = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

# dengan list comprehension
data_angka_sorted = [x for x in data_angka if x <= 5]
print(data_angka_sorted)

# dengan function biasa
def ganjil(angka):
    return angka%2 == 1
    

angka_ganjil_Fbiasa = list(filter(ganjil, data_angka)) # memanggil function 'ganjil' tanpa input argument karena argumentnya otomatis terisi dengan tiap-tiap item dalam list
print(f'hasil menggunakan filter function biasa = \n{angka_ganjil_Fbiasa}')

# filter dengan lambda untuk angka genap
angka_genap_lambda = list(filter(lambda x:x%2==0, data_angka))
print(f'hasil menggunakan filter lambda function = \n{angka_genap_lambda}')

# filter dengan lambda untuk kelipatan 5
kelipatan_lima = list(filter(lambda x:x%5==0, data_angka))
print(f'hasil kelipatan lima using lambda =\n{kelipatan_lima}')