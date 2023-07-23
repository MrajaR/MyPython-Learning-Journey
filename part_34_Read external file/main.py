## Tutorial membaca file external

print(3*"="," Membaca File txt ", 3*"=")
## MEMBUKA FILE
file = open("part_34_Read external file\data.txt",mode='r')

## MENGECEK apakah file dapat dibaca atau tidak dengan method readable()
# hasil true atau false tergantung dari mode yang digunakan untuk membuka file tersebut
print(f"status read = {file.readable()}")

## MENGECEK apakah file dapat ditulis/write atau tidak dengan method writable()
# hasil true atau false tergantung dari mode yang digunakan untuk membuka file tersebut
print(f"status write = {file.writable()}")

## MEMBACA FILE

print(f"\n {file}\n") # file sudah sudah terbuka,tapi hanya berisikan keterangan saja
# untuk bisa menampilkan isi file kita gunakan method read() 
# atau readline() (readline membaca file baris per baris/line per line )
# dan juga readlines() untuk membaca semua baris sebagai list

# baca seluruh file
print(file.read())

# baca per baris
# *note, argument "end=" berguna utk memodifikasi/menghilangkan karakter diakhir baris
# jika end='' artinya tidak ada karakter ataupun enter diakhir baris
# print(file.readline(),end='') # baca baris pertama
# print(file.readline(),end='') # baca baris kedua
# print(file.readline(),end='') # baca baris ketiga

# baca semua baris sebagai list
# tiap" item pada listnya adalah baris pada file (item pertama pada list adalah baris 1 pada file, dan sterusnya)
# print(file.readlines())

## mengetahui apakah file sudah diclose atau belum dengan "closed"
# setiap kali membuka file kita harus menutupnya diakhir
print(f"apakah file sudah diclose = {file.closed}")

# cara menutup/mengclose file menggunakan method close() *tanpa diprint
file.close()

print(f"\napakah file sudah diclose = {file.closed}")

## TEKNIK LAIN UNTUK MEMBUKA FILE DI PYTHON
# dengan menggunakan keyword 'with' kita tidak mesti menutup filenya lagi dengan manual menggunakan 'close()'
# file akan otomatis close ketika keluar dari local scope with

print("\n", 3*"="," Membaca File txt dengan with ", 3*"=")

with open("part_34_Read external file\data.txt", mode='r') as file:
    content = file.readline()
    print(content,end='')
    print(f"apakah file sudah diclose = {file.closed}")

print(f"apakah file sudah diclose = {file.closed}")
















