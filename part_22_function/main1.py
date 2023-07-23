### fungsi dengan argumen/parameter/input

## struktur fungsi:
# def nama_fungsi(argument/parameter/input):
#       badan fungsi

def hello_world(nama): # argument 'nama' ibarat variabel kosong yang siap menampung data/item apapun
    print(f'selamat datang di dunia wahai {nama}')

# memanggil function hello_world() dan mempassing 'sydmen' ke dalam argument 'nama'
hello_world('sydmen') # dapat mempassing tipe data apapun ke dalam argument

## membuat function dengan 2 argument sekaligus
def tambah(angka_1, angka_2): # argument 'angka_1' dan 'angka_2' ibarat variabel kosong yang siap menampung data/item apapun
    hasil = angka_1 + angka_2
    print(f'hasil dari {angka_1} + {angka_2} =  {hasil}')

# memanggil function tambah() dan mempassing integer 5 dan 6 ke dalam argument angka_1 dan angka_2 secara berurutan
tambah(5,6) # dapat mempassing tipe data apapun ke dalam argument
tambah(102,23)

def say_hi(orang_orang): # variabel apapun yang dipass di argument 'orang-orang' akan berubah nama variabelnya menjadi orang_orang
    ## orang_orang[0] = 'raja' # jika ini dilakukan maka akan merubah list people diluar function
    data_orang = orang_orang.copy() # oleh karena itu kita mesti membuat copy-an dari listnya disini
    for orang in data_orang:
        print(f'selamat {orang}, anda telah menjadi sukses!!')
    

people = ['sydmen','markus','dante']

# memasukkan/mampassing variabel list people ke dalam argument 'orang_orang' di function say_hi()
say_hi(people) # variabel list people akan berubah menjadi variabel list orang_orang (sesuai dengan argument di function say_hi()) 
