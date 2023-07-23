# fungsi dari file __init__ adalah untuk chaining, 
# yakni mengaitkan folder package dengan modul di dalamnya,
# ini berlaku jika kita hanya mengimport packagenya saja
# ketika kita hanya mengimport packagenya saja maka kita tidak bisa menggunakan modul didalamnya jika tanpa __init__


import sains

hasil_kinetik = sains.pisika.energi_kinetik(2,3)

print(f'hasil energi kinetik {hasil_kinetik}')

hasil_tambah = sains.tambah(1,2,3)
print(f'hasil tambah {hasil_tambah}')

hasil_pangkat3 = sains.matematika.scientific.pangkat(3)
print(f'hasil dari pangkat 3 = {hasil_pangkat3(5)}')

hasil_kali = sains.kali(2,3)
print(f'hasil kali {hasil_kali}')



























