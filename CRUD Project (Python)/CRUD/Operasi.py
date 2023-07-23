from .  import Database
from .util import random_string
import time
import os

def delete(no_buku):
    try:
        with open(Database.DB_NAME,'r') as file: # diread terlebih dahulu databasenya
            counter = 0
            
            while(True):
                content = file.readline() # membaca data.txt secara perbaris (setiap looping kembali ke atas maka baris selanjutnya akan diread)

                if len(content) == 0: # jika semua baris telah dipindahkan ke data_temp dan data yang dihapus sudah semuanya di keep di data awal, maka break
                    break
                elif counter == no_buku - 1: # jika saat giliran counter sama dengan index buku yang ingin dihapus maka data buku tsb tetap berada di data.txt awal, tidak dipindahkan ke data_temp
                    pass
                else: # jika selain dari pada kedua kondisi di atas maka data dari tiap" baris readline yang lain akan dipindahkan ke file data_temp (nanti data.txt yang diawal, akan dihapus dan datatemp dirubah menjadi data.txt lagi)
                    with open('data_temp.txt','a',encoding='utf-8') as temp_file:
                        temp_file.write(content)

                counter += 1

    except Exception as e:
        print('Failed to delete the data', type(e))

    try:
        os.rename('data_temp.txt',Database.DB_NAME) # mereplace data.txt yang berisikan data yang ingin dihapus dengan data_temp (file simpanan utk data yang ingin di keep), jadi pada akhirnya data.tx terhapus dan digantikan dengan data_temp yang dirubah menjadi data.txt lagi
    except:
        os.replace('data_temp.txt',Database.DB_NAME)

def update(no_buku,pk,date_add,penulis,judul,tahun):
    data = Database.TEMPLATE.copy()

    # mengisi key dari dictionary data dengan value yang baru (value berdasarkan input dari user)
    data['pk'] = pk
    data['date_add'] = date_add
    data['penulis'] = penulis + Database.TEMPLATE['penulis'][len(penulis):] 
    data['judul'] = judul + Database.TEMPLATE['judul'][len(judul):] 
    data['tahun'] = str(tahun)

    # hasil dari operasi dictionary dimasukkan ke dalam variabel data_str
    data_str = f"{data['pk']},{data['date_add']},{data['penulis']},{data['judul']},{data['tahun']}\n" # tidak perlu diberi enter diakhir, dari awal input user di modul view.py juga sudah dihilangkan enter di bagian variabel tahun, dgn tujuan tidak merusak mode r+

    # update menggunakan mode r+
    panjang_data = len(data_str)

    try:
        with open(Database.DB_NAME,'r+',encoding='utf-8') as file:
            file.seek(panjang_data*(no_buku-1))
            file.write(data_str)
    except:
        print("failed to update file")

def create(penulis,judul,tahun):
    data = Database.TEMPLATE.copy()

    # mengisi key dari dictionary data dengan value yang baru (value berdasarkan input dari user)
    data['pk'] = random_string(6)
    data['date_add'] = time.strftime('%Y-%m-%d-%H-%M-%S%z',time.gmtime())
    data['penulis'] = penulis + Database.TEMPLATE['penulis'][len(penulis):] 
    data['judul'] = judul + Database.TEMPLATE['judul'][len(judul):] 
    data['tahun'] = str(tahun)

    # hasil dari operasi dictionary dimasukkan ke dalam variabel data_str
    data_str = f"{data['pk']},{data['date_add']},{data['penulis']},{data['judul']},{data['tahun']}\n" # karena data['tahun'] tidak memiliki enter (value dari data['tahun] adalah dari input user di modul view.py makanya tidak ada enter) maka ditambahkan '\n', agar ketika meappend data sekaligus membuat baris baru untuk data berikutnya yang akan dibuat

    try: 
        with open(Database.DB_NAME,'a',encoding='utf-8') as file: # begini karena ingin menambahkan data maka meenggunakan mode append, jika menggunakan write yang ada malah di overwrite data yang sebelumnya
            file.write(data_str)
    except: # jika block try error maka akan pindah ke blok except dan menjalankan print berikut
        print("Failed to add another Data Book")


def create_first_data(): # function untuk membuat file pertama
    penulis = input('penulis : ')
    judul = input('Judul : ')
    while(True):
        try:
            tahun = int(input('tahun\t: '))
            if len(str(tahun)) == 4: # jika input tahun dari user 4 digit maka akan berhasil dan break dari loop
                break
            elif len(str(tahun)) < 4 or len(str(tahun)) > 4:
                print('angka dalam tahun harus 4 digit') # jika input lebih dari 4 atau kurang dari 4 maka akan menampilkan berikut
        except: # jika block try error maka akan pindah ke blok except dan menjalankan print berikut
            print('tahun harus berupa angka')

    data = Database.TEMPLATE.copy() # mengambil copyan dari template database di database.py

    # mengisi key dari dictionary data dengan value yang baru (value berdasarkan input dari user)
    data['pk'] = random_string(6)
    data['date_add'] = time.strftime('%Y-%m-%d-%H-%M-%S%z',time.gmtime())
    data['penulis'] = penulis + Database.TEMPLATE['penulis'][len(penulis):] 
    data['judul'] = judul + Database.TEMPLATE['judul'][len(judul):] 
    data['tahun'] = str(tahun)

    data_str = f"{data['pk']},{data['date_add']},{data['penulis']},{data['judul']},{data['tahun']}\n"
    try:
        with open(Database.DB_NAME,'w',encoding='utf-8') as file:
            file.write(data_str)
    except:
        print("Failed to Write Data")

def read(**kwargs):
    try:
        with open(Database.DB_NAME,'r') as file:
            content = file.readlines() # membaca file dengan menampilkannya sebagai list, item" pada listnya adalah tiap" baris pada filenya
            jumlah_buku = len(content)
            if 'index' in kwargs: # jika ada keyword argument index digunakan dalam function ini
                index_buku = kwargs['index']-1
                if index_buku < 0 or index_buku >= jumlah_buku: # jika pilihan user tidak sesuai dengan index buku yang tersedia
                    return False
                else:
                    return content[index_buku]
            else:
                return content # jika tidak ada argument/keyword argument/kosongan dalam function ini maka return content yang berisikan list yang tiap" itemnya adalah  string yang mengandung pk,date_add,penulis,judul,tahun
    except Exception as e:
        print(f'tipe exception = {type(e)}')
        print('failed to read data')
        return False

