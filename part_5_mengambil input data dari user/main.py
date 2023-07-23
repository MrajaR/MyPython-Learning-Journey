# data yang dimasukkan ke dalam input pasti string


# data dalam input pasti berbentuk string
data = input("masukkan data :")
print("data =", data, "type =", type(data))

# jika kita ingin merubahnya tipe data string dalam input menjadi tipe data lain maka harus dicasting 

angka = float(input("masukkan angka ="))
angka = int(input("masukkan angka ="))

print("data =", angka, ",type =", type(angka)) 
"""tipe data berubah menjadi integer
karna secara urutan baris, casting yang terakhir adalah casting data
'angka' menjadi int"""

# jika ingin dicasting ke boolean maka seperti ini :
biner = bool(int(input("masukkan nilai boolean : ")))
print("data =", biner, ",type =", type(biner))
 
"""jika dicasting menjadi integer dulu 
(nested casting didalam castingan boolean)
baru lah tipe data dapat bernilai false (jika integer = 0)"""