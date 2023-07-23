from . import Operasi

DB_NAME = 'data.txt'
# template dictionary untuk pengolahan file
TEMPLATE = {
    'pk':'XXXXXX',
    'data_add':"yyyy-mm-dd",
    'judul':255*' ',
    'penulis':255*' ',
    'tahun':'yyyy'
}

def init_console():
    try:
        with open(DB_NAME,'r') as file:
            print('database tersedia, init done!')
    except:
        print('Database tidak ditemukan, silahkan membuat database baru')
        Operasi.create_first_data() # jika belum ada filenya, maka akan menjalankan function ini