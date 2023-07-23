# list kumpulan angka
data_angka = [1,5,2,3]
print(data_angka)

# list kumpulan data string
data_string = ['raja','fadli','masnita']
print(data_string)

# list kumpulan boolean
data_bool = [True, False, True, False]
print(data_bool)

# list campuran tipe data
data_campuran = [1,'markus', True, 'dealift', 2.7, False]
print(data_campuran)

# cara alternatif utk membuat list
print('\ncara alternatif membuat list') # range(start,stop,kelipatan)
data_range = range(0,10,2)
print(data_range)
print(list(data_range)) # method list() untuk merubahnya menjadi list

# membuat list dengan for loop (list comprehension)

print('\nmembuat list comprehension')
list_dengan_for = [angka for angka in range (10)]
print(list_dengan_for)

# membuat list angka genap, dengan metode list comprehension
list_for_1 = [x for x in range(0,20) if x%2 == 0]
print(list_for_1)
# cara baca list_for_1:
# buatlah list berisikan x yang mana x adalah item-item dalam range(10), syaratnya jika x dimoduluskan dengan 2 hasilnya 0

# membuat list angka ganjil, dengan metode list comprehension
list_for_2 = [x for x in range(0,20) if x%2 == 1]
print(list_for_2)
# cara baca list_for_2:
# buatlah list berisikan x yang mana x adalah item-item dalam range(0,20), syaratnya jika x dimoduluskan dengan 2 hasilnya 1

list_for_3 = [x**2 for x in range(10)]
print(list_for_3)
# cara baca list_for_3:
# buatlah list berisikan x yang dipangkatkan 2, yang mana x adalah item-item dalam range(10)


list_for_4 = [x for x in range(10) if x != 5] 
print(list_for_4)
# cara baca list_for_4:
# buatlah list berisikan x yang mana x adalah item-item dalam range(10), syaratnya x tidak boleh ada 5

buah = ['mangga','jambu','apel','nanas','kuaci','pisang']

new_list_buah = [x if x != 'jambu' else 'pisang' for x in buah]
print(new_list_buah)
# cara baca new_list_buah:
#buatlah list berisikan x dengan syarat(if) x tidak boleh(!=) ada jambu tetapi(else) pisang, yang mana(for) x adalah tiap item-item dalam(in) list buah
# jika ada 'else' dalam list comprehension maka didahulukan statement if dan elsenya lalu baru statement for nya