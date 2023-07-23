# looping dari list

# menggunakan for loop 
kumpulan_angka = [1,2,4,7,2,5,1,3]
 
for angka in kumpulan_angka:
    print(f'angka = {angka}')

peserta = ['sydmen','markus','dante','luciper','moza']

for nama in peserta:
    print(f'nama peserta = {nama}')

# menggunakan for loop dan range 
kumpulan_angka = [10,11,5,2,0,2,45]

for i in range(len(kumpulan_angka)): # maksudnya membuat loop untuk tiap" data/item di kumpulan_angka berdasarkan indexnya
    print(f'angka = {kumpulan_angka[i]}')

# menggunakan while
kumpulan_angka = [10,11,5,2,0,2,45]

i = 0

while i < len(kumpulan_angka):
    print(f'angka (using while loop) = {kumpulan_angka[i]}')
    i += 1

# menggunakan list comprehension
data = ['markus','17','sydmen','23','fadli','18']

[print(f'data = {i}') for i in data]

# looping menggunakan metode list comprehension dengan syarat (if)
new_data = [x for x in data if 'a' in x]
print(f'hasil list comprehension dengan if(syarat) :\n {new_data}')


# menggunakan enumerate
data_list = ['markus',17,'sydmen',23,'fadli',18]

for index,data in enumerate(data_list): # variable index sebenarnya bisa dideclare dengan nama bebas(entah itu x,i,y dll), yg maknanya menunjukkan index ke-sekian dari suatu data, variabel itu sendiri bisa menunjukkan/menghitung index karena adanya method enumerate()
    print(f'index = {index}, data = {data}')

# atau bisa juga seperti ini
for i in data_list:
    print(f'index ke = {data_list.index(i)}, datanya = {i}')
