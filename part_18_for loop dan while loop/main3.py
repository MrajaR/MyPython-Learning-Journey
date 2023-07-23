## NESTED FOR LOOP

ukuran = ['besar', 'kecil', 'sedang']
buah = ['mangga', 'apel', 'semangka']

for x in ukuran: # untuk tiap-tiap item pada list ukuran lakukanlah:
    # untuk setiap iterasi dari tiap-tiap item di list ukuran lakukanlah loop berikut:
    for y in buah: # untuk tiap-tiap item dalam list buah lakukanlah:
        print(f'ukuran = {x}, buah = {y}') # value dari x (outer loop) tidak akan berubah sampai inner loopnya pindah iterasi selanjutnya

# CARA BACANYA:
# iterasi ke-1 dari outer loop (untuk value 'besar') : untuk value/item 'besar' lakukan lah for loop di list buah, 
# - for loop di list buah akan melakukan print untuk value/item 'besar' dan value/item pertama di list buah yakni 'mangga'
# - for loop di list buah akan melakukan print untuk value/item 'besar' dan value/item kedua di list buah yakni 'apel'
# - for loop di list buah akan melakukan print untuk value/item 'besar' dan value/item ketiga di list buah yakni 'semangka'

# iterasi ke-2 dari outer loop (untuk value 'kecil') : untuk value/item 'kecil' lakukan lah for loop di list buah, 
# - for loop di list buah akan melakukan print untuk value/item 'kecil' dan value/item pertama di list buah yakni 'mangga'
# - for loop di list buah akan melakukan print untuk value/item 'kecil' dan value/item kedua di list buah yakni 'apel'
# - for loop di list buah akan melakukan print untuk value/item 'kecil' dan value/item ketiga di list buah yakni 'semangka'
  
# iterasi ke-3 dari outer loop (untuk value 'sedang') : untuk value/item 'sedang' lakukan lah for loop di list buah, 
# - for loop di list buah akan melakukan print untuk value/item 'sedang' dan value/item pertama di list buah yakni 'mangga'
# - for loop di list buah akan melakukan print untuk value/item 'sedang' dan value/item kedua di list buah yakni 'apel'
# - for loop di list buah akan melakukan print untuk value/item 'sedang' dan value/item ketiga di list buah yakni 'semangka'

for x in range(2):
    print("This is the outer loop iteration number " + str(x))
    for y in range(3+1):
        print("Inner loop iteration number " + str(y))
    print("Exit inner loop")  


for left in range (7): # untuk tiap-tiap item dalam range angka 0-6 lakukanlah:
    # lakukanlah loop ini untuk tiap-tiap item yang diiterasi pada loop diatasnya
    for right in range(left,7): 
        print('tes', left, right, end=' ')
    print()