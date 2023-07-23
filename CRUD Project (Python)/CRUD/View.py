from . import Operasi

def delete_console():
    read_console()
    while(True):
        print('Silahkan pilih nomor buku yang ingin didelete')
        no_buku = int(input("Nomor Buku: "))
        data_buku = Operasi.read(index=no_buku)
        
        if data_buku:
            data_break = data_buku.split(',')
            pk = data_break[0]
            date_add = data_break[1]
            penulis = data_break[2]
            judul = data_break[3]
            tahun = data_break[4][:-1] # [:-1] agar enter di paling belakang tidak diambil

            # DATA YANG INGIN DIHAPUS (PENULIS, JUDUL, DAN TAHUN)
            print('\n'+"="*100)
            print("Berikut adalah data yang akan dihapus")
            print(f"1. Penulis\t: {penulis:.40}")
            print(f"2. Judul\t: {judul:.40}")
            print(f"3. Tahun\t: {tahun:4}")
            is_done = input("Apakah anda yakin? (y/n)? ")
            if is_done == 'Y' or is_done == 'y':
                Operasi.delete(no_buku)
                break           
            
        else:
            print('nomor tidak valid, silahkan masukkan nomor lagi')

    print("Data berhasil dihapus")

def update_console():
    read_console()
    while(True):
        print('Silahkan pilih nomor buku yang ingin diupdate')
        no_buku = int(input("Nomor Buku: "))
        data_buku = Operasi.read(index=no_buku)
        
        if data_buku:
            break
        else:
            print('nomor tidak valid, silahkan masukkan nomor lagi')

    data_break = data_buku.split(',')
    pk = data_break[0]
    date_add = data_break[1]
    penulis = data_break[2]
    judul = data_break[3]
    tahun = data_break[4][:-1] # [:-1] agar enter di paling belakang tidak diambil

    while(True):
        # DATA YANG INGIN DIUBAH (PENULIS, JUDUL, DAN TAHUN)
        print('\n'+"="*100)
        print("Silahkan pilih data apa yang ingin anda ubah")
        print(f"1. Penulis\t: {penulis:.40}")
        print(f"2. Judul\t: {judul:.40}")
        print(f"3. Tahun\t: {tahun:4}")

           

        # MEMILIH MANA YANG INGIN DIRUBAH DAN MERUBAHNYA
        user_option = input("Pilih data [1,2,3]: ")
        print('\n'+"="*100)

        match user_option:
            case '1': penulis = input('Penulis\t: ')
            case '2': judul = input('Judul\t: ')
            case '3':     
                while(True):
                    try:
                        tahun = int(input('tahun\t: '))
                        if len(str(tahun)) == 4:
                            break
                        else:
                            print('angka dalam tahun harus 4 digit')
                    except:
                        print('tahun harus berupa angka')
            case _: print('INDEX TIDAK ADA')

        print("Berikut Data Baru Anda")
        print(f"1. Penulis\t: {penulis:.40}")
        print(f"2. Judul\t: {judul:.40}")
        print(f"3. Tahun\t: {tahun:4}")
        is_done = input("Apakah data sudah sesuai update? (y/n)? ")
        if is_done == 'Y' or is_done == 'y':
            break

    Operasi.update(no_buku,pk,date_add,penulis,judul,tahun)

def create_console():
    print('\n\n','='*100)
    print('silahkan tambah data buku\n')
    penulis = input('penulis\t: ')
    judul = input('judul\t: ')
    while(True):
        try:
            tahun = int(input('tahun\t: '))
            if len(str(tahun)) == 4:
                break
            else:
                print('angka dalam tahun harus 4 digit')
        except:
            print('tahun harus berupa angka')
    

    Operasi.create(penulis,judul,tahun)
    print('\nBerikut adalah data baru anda')
    read_console()

    

def read_console():
    data_file = Operasi.read() # variabel data file berupa list yang setiap itemnya berisi pk,date_add,penulis,judul,tahun dalam satu komponen string
    
    index = 'No'
    judul = 'Judul'
    penulis = 'Penulis'
    tahun = 'Tahun'

    # Header
    print('\n'+'='*100)
    print(f'{index:4} | {judul:40} | {penulis:40} | {tahun:5}')
    print('-'*100)
    
    # Data
    for index,data in enumerate(data_file):
        data_break = data.split(',') # dipisahkan dibagian yang ada komanya, sehingga tiap" item dalam listnya dipecah menjadi pk,date_add,penulis,judul, dan tahun (sebelum loop ini dibuat aslinya kelima itu bersatu menjadi 1 item di list)
        pk = data_break[0]
        data_add = data_break[1]
        penulis = data_break[2]
        judul = data_break[3]
        tahun = data_break[4]
        
        print(f'{index+1:4} | {judul:.40} | {penulis:.40} | {tahun:4}',end='')




    # Footer
    print('='*100+'\n')

