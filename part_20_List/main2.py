## operasi list

# index  0(-3)     1(-2)    2(-1)
data = ['dante', 'sydmen', 'markus']

# mengambil data dari list (indexing)
data_0 = data[0] # bisa juga menggunakan index -3
print(f'data list index 0 = {data_0}')

data_terakhir = data[-1] # bisa juga menggunakan index 2
print(f'data list index terakhir = {data_terakhir}')

# mengambil info jumlah item
jumlah_item_list = len(data)
print(f'jumlah item dalam list = {jumlah_item_list}')


## manipulasi list
# menambahkan item pada list sesuai posisi yang diinginkan
print(f'\ndata list sebelum ditambahkan = \n{data}')
data.insert(1,'dukun')
print(f'data list setelah ditambahkan = \n{data}')

# menambahkan item pada list diakhir index list
print(f'\ndata list sebelum ditambahkan = \n{data}')
data.append('patur') # menambahkan item di index terakhir
print(f'data list setelah ditambahkan = \n{data}')

# menggabungkan list
data_baru = ['aris','aqila','opi']
print(f"\nada data list baru = \n{data_baru}")
data.extend(data_baru) # tidak perlu dimasukkan ke dalam variabel
print(f'hasil gabungan dengan data list baru = \n{data}')


# merubah item pada list
data[1] = 'padli'
print(f'\nlist setelah dirubah = \n{data}')

# menghapus data
data_yg_dipop = data.pop() # menghapus item pada index terakhir
print(f'\ndata setelah dihapus dengan pop = \n{data}')
print(f'data yang di pop = {data_yg_dipop}')

data.remove('padli')
print(f'\n list setelah dihapus menggunakan remove() = \n{data} ')
