### membuat fungsi (disebut juga method, subrutin atau rutin)

## misal ingin buat program untuk print hello world 5x utk dipakai berkali"
## tentu dengan cara seperti ini akan memakan banyak waktu dan tidak menerapkan prinsip "don't repeat your code"
# print("hello world")
# print("hello world")
# print("hello world")
# print("hello world")
# print("hello world")

## maka solusinya adalah dengan membuat sebuah fungsi sbg berikut:
def hello_world(): # mendefinisikan fungsi
    print("hello world")
    print("hello world")
    print("hello world")
    print("hello world")
    print("hello world\n")

## setelah mendefinisakan fungsi, maka kita harus memanggil fungsinya agar keluar outputnya
## dan ini dapat kita panggil berkali-kali sesuai keinginan kita
hello_world()

## contoh lain
def hello_nama():
    print('hello sydmen chicken leg')
    print('hello teman-teman ku')
    print('hello markus horison')

## memanggil function hello_nama()
hello_nama()











