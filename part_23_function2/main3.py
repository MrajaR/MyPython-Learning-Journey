### penggunaan **kwargs (keyword arguments) pada function

## hampir mirip dengan *args, hanya saja **kwargs digunakan untuk menginput data dengan keyword ke dalam argument (keyword argument)
## jika kwargs di print atau di return didalam function maka akan menghasilkan output dictionaries
## walaupun banyak keyword argument yang diinput ke dalam argument saat pemanggilan function,
## ketika membuat functionnya kita hanya perlu membuat satu argument yakni **kwargs

def fungsi(nama, tinggi, berat):
    '''fungsi biasa dengan banyak argument '''
    print(f'{nama} punya tinggi {tinggi} cm dan berat {berat} kg')

fungsi('raja',180, 83)

def fungsi_kedua(**kwargs):
    x = kwargs['nama'] # mengakses value melalui key yang di input di pemanggilan fungsi ini di bawah
    y = kwargs['tinggi'] # mengakses value melalui key yang di input di pemanggilan fungsi ini di bawah
    z = kwargs['berat'] # mengakses value melalui key yang di input di pemanggilan fungsi ini di bawah
    print(f'{x} punya tinggi {y} cm dan berat {z} kg')


fungsi_kedua(nama='ucup',tinggi=200,berat=120) # dapat menginput lebih dari satu keyword argument pada pemanggilan fungsi walaupun pada fungsinya hanya terdapat satu argument yakni **kwargs

def fungsi_ketiga(**kwargs):
    print(kwargs) # akan menghasilkan output berupa dictionary jika di panggil

fungsi_ketiga(nama = 'raja') # outputnya akan dict dengan key 'nama' dan value 'raja'

def fungsi_keempat(**kwargs):
    return kwargs

tes = fungsi_keempat(nama = 'sydmen fungsi keempat')    
print(f'\n{tes}')
## studi kasus (mencampur *args dan **kwargs)

# def math(**kwargs, *args): # error karena keyword argument (**kwargs) harus muncul dibelakang setelah positional argument (*args)

def math(*args,**kwargs):
    if kwargs['option'] == 'tambah': # cara bacanya, jika keyword argument (kwargs) dengan key 'option' dan value nya 'tambah' maka lakukan...
        output = 0
        for x in args:
            # output = 0 # malah akan mereset output ke 0 setiap kali terjadi loop
            output += x # jika += begini, maka output langsung berubah, tidak perlu buat variabel 'output' lagi untuk menampung hasil barunya seperti misal "output= output + x"
    
    elif kwargs['option'] == 'kali':
        output = 1
        for x in args:
            # output = 0 # malah akan mereset output ke 0 setiap kali terjadi loop
            output *= x # jika *= begini, maka output langsung berubah, tidak perlu buat variabel 'output' lagi untuk menampung hasil barunya seperti misal "output= output + x"
    
    else:
        print('tidak ada hasil')

    return output # return ditempatkan di akhir function


hasil = math(1,2,3,4,option = 'tambah')
print(f'\nhasil dari fungsi campuran kwargs dan args = {hasil}')