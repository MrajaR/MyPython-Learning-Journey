# operator dictionary

data_dict = {
    "syd":"syanda",
    'markus':'arvino',
    'charles':'raja',
    'dukun':'ardiles'
}

## mengecek key exist atau tidak
print('syd' in data_dict)
# ngikutin kelas terbuka
key = 'syd'
check = key in data_dict
print(f'apakah {key} ada di data_dict : {check}')

## mengakses value dalam dict menggunakan method get()
# cara yg kurang baik
print(data_dict['charles'])
# yang baik dengan method get()
print(data_dict.get('charles'))
# method get() juga bisa seperti ini (bila key tidak ada maka akan menampilkan 'key tidak ada')
print(data_dict.get('dante','key tidak ada'))

## mengupdate data dictionary
# cara kurang baik
data_dict['syd'] = 'sydmen99' # meupdate value dari key syd
print(data_dict)
data_dict['iduy'] = 'maypitnes' # mengupdate key dan value baru, dan ditambahkan di ujung/akhir dict
print(data_dict)

# cara yang lebih baik menggunakan  method update()
data_dict.update({'syd':'syanda sydmen'}) # meupdate value dari key syd
print(data_dict)
data_dict.update({'gay':'maypitnes'}) # mengupdate key dan value baru, dan ditambahkan di ujung/akhir dict
print(data_dict)

# delete data pada dictionary
del data_dict['iduy']
print(data_dict)
