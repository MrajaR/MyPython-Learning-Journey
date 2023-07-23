### copy dictionary

teman_teman = {
    "syd":"syanda shopee food",
    'markus':'arvino sabron',
    'charles':'raja ngoding',
    'dukun':'pencari hantu',
    'lucy':'luqman darmawan'
}

## mengcopy/menduplikat dict dengan cara yang salah, 
# jika begini perubahan yg diterapkan pada salah satu list akan diterapkan juga pada list yang lain
friends = teman_teman

print(f'teman-teman = {teman_teman}')
print(f"friends = {friends}")

friends.update({'iduy':'maypitness'})
print(f'\nteman-teman = {teman_teman}')
print(f"friends = {friends}")

## mengcopy/menduplikat dict dengan method copy() *sama dgn copy list*
print('\n'+'='*5 + 'mengcopy menggunakan method copy()' + '='*5)
friends = teman_teman.copy()

print(f'teman-teman = {teman_teman}')
print(f"friends = {friends}")

del friends['iduy']
print(f'\nteman-teman = {teman_teman}')
print(f"friends = {friends}")

## method pop() dictionary *dapat memilih utk nge pop berdasarkan key*
# data = friends.pop() # tidak bisa, pop di dict mesti ada argumentnya
# print(data)
print('\n' + '-'*5 + 'pop dictionary' + '-'*5)
data_dukun = friends.pop('dukun') # mengeluarkan key dukun dan valuenya dari dict friends dan mempassingnya ke variabel data_dukun
print(f'data dukun = {data_dukun}')
# setelah dict friends di print lagi, sudah tidak ada key dukun dan valuenya
print('friends = {}'.format(friends)) # bentuk lain dari string formatting

## method popitem() dictionary *akan nge pop item paling ujung/terakhir*
# data_terakhir = friends.popitem('syd') # tidak bisa, tidak ada argumen utk method popitem()
print('\n' + '-'*5 + 'pop item dictionary' + '-'*5)
data_terakhir = friends.popitem() # mengeluarkan key dan value paling terakhir dari dict friends dan mempassingnya ke variabel data_terakhir
print('data terakhir = {}'.format(data_terakhir)) # bentuk lain dari string formatting
# setelah dict friends di print lagi, sudah tidak ada key dan value terakhir/paling ujung
print(f'friends = {friends}')