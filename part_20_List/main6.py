# deep copy nested list

data_0 = ['markus','laki-laki',18,]
data_1 = ['sydmen','wanita',23]

data_2D = [data_0, data_1, 'sabron']
data_2D_copy = data_2D.copy()

print(f'data_2D = {data_2D}')
print(f'data_2D_copy = {data_2D_copy}')

# mengambil data/item utk nested list

print(data_2D[0][1]) 
# indexing yg pertama utk item index ke-0 pada variabel list data_2D
# indexing yg kedua untuk item index ke-1 pada variabel list di index ke-0 pada list_2D

## problem dengan reference
# address utk variabel data_2D dan data_2D_copy
# addressnya berbeda (terduplikasi dengan baik)

print(f'\naddress data_2D = {hex(id(data_2D))}')
print(f'address data_2D_copy = {hex(id(data_2D_copy))}\n')

# akan tetapi untuk address dari list di dalamnya(contoh disini list di index ke-0) tidak berubah/sama, oleh karenanya jika list di index ke-0 tsb dirubah maka duplikasinya pun ikut berubah 
print('address dari index ke-0')
print(f'address index-0 data_2D = {hex(id(data_2D[0]))}')
print(f'address index-0 data_2D_copy = {hex(id(data_2D_copy[0]))}\n')

data_2D[1][0] = 'Genderuwo' # merubah index ke-0 pada item(yakni list) di index ke-1 pada data_2D, yang kemudian juga akan berubah di duplikasinya karena 1 reference (address yg sama)
data_2D[2] = 'icap' # merubah item index ke-2 pada list data_2D (tidak akan merubah isi dari duplikasinya karena addressnya berbeda)
print(f'\ndata_2D = {data_2D}')
print(f'data_2D_copy = {data_2D_copy}')


"""
item-item yang berupa list di dalam nested list jika di duplikasi akan mempunyai address yang sama(karena masih 1 reference),
tetapi jika didalamnya terdapat item/data yang bertipe selain list (int, string, boolean) 
akan memiliki address yang berbeda karena pasti akan diduplikasi dengan benar"""

# solusinya menggunakan deepcopy jika list nya adalah nested list

from copy import deepcopy

data_2D = [data_0, data_1, 'sabron']
data_2D_deepcopy = deepcopy(data_2D)

print(f'\naddress index-0 data_2D = {hex(id(data_2D[0]))}')
print(f'address index-0 data_2D_deepcopy = {hex(id(data_2D_deepcopy[0]))}\n')

data_2D[1][0] = 'sydmen'
print(f'data_2D = {data_2D}')
print(f'data_2D_copy = {data_2D_copy}')
print(f'data_2D_deepcopy = {data_2D_deepcopy}')