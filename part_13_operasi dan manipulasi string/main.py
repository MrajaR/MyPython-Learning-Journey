# operasi dan manipulasi string

# 1. menyambung string (concatenate) memakai tanda +
nama_pertama = "muhammad"
print("nama pertama = " + nama_pertama)
nama_tengah = "raja"
print('nama tengah = ' + nama_tengah)
nama_akhir = "reivan"
print("nama akhir = " + nama_akhir)

nama_lengkap = nama_pertama + ' ' + nama_tengah + ' ' + nama_akhir
print("nama lengkap saya adalah, " + nama_lengkap)

# 2. menghitung panjang string
panjang = len(nama_lengkap)
print("panjang dari str " + nama_lengkap + " = " + str(panjang))

# 3. operator untuk string

# mengecek apakah ada komponen char atau string di sebuah string

d = "d ra" 
status = d in nama_lengkap # melacak karakter secara berurutan
print(d + " ada di " + nama_lengkap + " = " + str(status))

d = "RAJA" 
status = d in nama_lengkap # melacak karakter secara berurutan
print(d + " ada di " + nama_lengkap + " = " + str(status))

d = "RAJA" 
status = d not in nama_lengkap # melacak karakter secara berurutan
print(d + " tidak ada di " + nama_lengkap + " = " + str(status))

# mengulang string
print(10*"wk")
print("wk"*10)

#indexing
print("index ke-0 : " + nama_lengkap[0])
print("index ke-6 : " + nama_lengkap[6])
print("index ke-(-1) : " + nama_lengkap[-1])
print("index ke-(-2) : " + nama_lengkap[-2])
# index slicing
print("index ke-0 sampai 3 : " + nama_lengkap[0:4]) # dari index 0 - 3 yang diambil
print("index ke-3 sampai 9 : " + nama_lengkap[3:10]) # dari index 3 - 9 yang diambil
print("index ke-0,2,4,6,8,10 : " + nama_lengkap[0:11:2]) # dari index 0,2,4,6,8,10 yang diambil

# item paling kecil
print("paling kecil : " + min(nama_lengkap) ) # paling kecil disini adalh spasi, sesuai dengan urutan binary di ASCII 
print("paling besar : " + max(nama_lengkap)) # paling besar disini adalah huruf "v", sesuai dengan urutan binary di ASCII 

ASCII_tes = ord(" ")
print("ASCII code untuk spasi adalah : " + str(ASCII_tes))
ASCII_tes = ord("v")
print("ASCII code untuk v adalah : " + str(ASCII_tes))
dataTesASCII = 118
print("CHAR untuk ASCII ke 118 adalah : " + chr(dataTesASCII)) 
dataTesASCII = 65
print("CHAR untuk ASCII ke 65 adalah : " + chr(dataTesASCII)) 

# 4. operator dalam bentuk method

data = "saya akan menjadi programmer hebat dan kaya"
jumlah = data.count("a")
print("jumlah huruf a pada " + data + " " + str(jumlah))