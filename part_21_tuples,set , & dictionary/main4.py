teman_teman = {
    "syd":"syanda shopee food",
    'markus':'arvino sabron',
    'charles':'raja ngoding',
    'dukun':'pencari hantu',
    'lucy':'luqman darmawan'
}

## mengakses dan looping key
for teman in teman_teman: # teman merujuk pada tiap-tiap key secara berurutan
    print(teman) # jika begini, maka outputnya adalah keynya saja, dan juga ini cara yg kurang baik untuk mengakses key

# mengakses, dan looping key menggunakan method key(), ini cara terbaik
teman = teman_teman.keys()
print(teman)

for teman in teman_teman.keys():
    print(teman) # seperti ini lebih baik, karena kita jadi tau jika loop ini untuk dict, bukan list biasa

## mengakses values
for teman in teman_teman: # teman merujuk pada tiap-tiap key secara berurutan
    print(teman_teman[teman]) # jika begini, maka outputnya adalah value nya saja, dan juga ini cara yg kurang baik untuk mengakses value

for teman in teman_teman.keys():
    print(teman_teman.get(teman)) # seperti ini lebih baik, karena kita jadi tau jika loop ini untuk dict, bukan list biasa

# mengakses, dan looping value menggunakan method values(), ini cara terbaik
value = teman_teman.values()
print(value)

for value in teman_teman.values():
    print(value) # seperti ini lebih baik, karena kita jadi tau jika loop ini untuk dict, bukan list biasa

# mengakses key dan value secara bersamaan menggunakan method items()
item = teman_teman.items()
print(item)

for item in teman_teman.items():
    print(item)

# bisa juga seperti ini
for key, value in teman_teman.items():
    print(f'key = {key}, value = {value}')