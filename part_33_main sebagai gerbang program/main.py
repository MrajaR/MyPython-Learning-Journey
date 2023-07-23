### __main__ adalah top level code environment

# int main() { << jika di c++/c

# }

# class Main(){ << jika di java
    
#     static void main(){

#     }
# }

# jika di python cukup dengan "print("Hello World")" sudah bisa jalan codenya

## implementasi __main__ di python ##

## __name__ = "__main__"

# __name__ pada file program utama
# jika begini maka output dari output dari __name__ adalah __main__, karena __name__ dijalankan langsung pada program utama
print(f"nilai __name__ pada main.py = '{__name__}'")

# __name__ pada file program external
# jika begini maka output dari __name__ adalah nama file external itu sendiri yakni "fungsi"
# karena aslinya program tsb terdapat pada file external (fungsi.py) yang diimport , bukan program di file di sini (main.py)
# tentu jika program ini dijalankan langsung pada file fungsi.py maka outputnya akan "__main__, karena __name__ dijalankan langsung pada program utama"
import fungsi

## CONTOH IMPLEMENTASI __main__ DI REALCASE ##

def fungsi_tambah(a:int,b:int)->int:
    return a+b

# 1. program yang hanya bisa dijalankan di file program utama, jika file ini diimport di file lain maka block if ini tidak akan jalan
if __name__ == "__main__": # >> sintaks if seperti ini lazim digunakan pada awal sbuah program, bisa dibilang seperti konvensi penulisan code pada python
    angka1 = 11
    angka2 = 9
    hasil = fungsi_tambah(angka1, angka2)
    print(f"hasil tambah {hasil}")

# 2. untuk membuat sintaks "python -m package_name"/"python package_name" di console

import package # << file __main__.py tidak berpengaruh apa, hanya berpengaruh di console