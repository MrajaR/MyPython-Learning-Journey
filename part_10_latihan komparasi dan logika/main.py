# # membuat gabungan area rentang dari angka

# # ++++++++3--------10+++++++++


inputUser = int(input('masukkan angka yang bernilai\nkurang dari 3 atau lebih besar dari 10 : '))

isKurangDari = inputUser < 3
print('kurang dari 3 = ', isKurangDari)

isLebihDari = inputUser > 10
print('lebih dari 10 = ', isLebihDari)

isCorrect = isKurangDari or isLebihDari
print('maka angka inputnya : ', isCorrect)

# -------3+++++++++10---------

inputUser = int(input('masukkan angka antara 3 sampai 10 : '))

condition_1 = inputUser >= 3
print('lebih dari sama dengan 3 : ', condition_1)
condition_2 = inputUser <= 10
print('kurang dari sama dengan 10 : ', condition_2)

isCorrect = condition_1 and condition_2
print('hasil dari angka yang anda input : ', isCorrect)


# --------0+++++++5-----8++++++11------
inputUser = int(input('masukkan angka antara 0 sampai 5 dan 8 sampai 11 : '))

condition1 = inputUser >= 0
print('lebih besar dari sama dengan 0 : ', condition1)
condition2 = inputUser <= 5
print('kurang dari sama dengan 5 : ', condition2)

condition3 = inputUser >= 8
print('lebih besar dari sama dengan 8 : ', condition3)
condition4 = inputUser <= 11
print('kurang dari sama dengan 11 : ', condition4)

isCorrect = condition1 ^ condition2 ^ condition3 ^ condition4
print('hasil dari angka yang anda input : ', isCorrect)

# ++++++++0-------5+++++8-------11+++++++++
print('       ')
inputUser = int(input('masukkan angka kurang dari 0\natau 5 sampai 8 atau lebih dari 11 :'))

condition1 = inputUser <= 0
print('kurang dari sama dengan 0 = ', condition1)
condition2 = inputUser >= 5
print('lebih dari sama dengan 5 = ', condition2)
condition3 = inputUser <= 8
print('kurang dari sama dengan 8 = ', condition3)
condition4 = inputUser >= 11
print('lebih dari sama dengan 11 = ', condition4)

isCorrect = condition1 or condition2 or condition3 or condition4
print('hasil dari angka yang anda input = ', isCorrect)