### PROJECT CRUD (CREATE, READ, UPDATE, DELETE)
## DATA BASENYA MENGGUNAKAN DATA.TXT

import os
import CRUD as CRUD

if __name__ == "__main__": # gerbang dari program
    sistem_operasi = os.name

    # match sistem_operasi: # jika sistem_operasinya match/sesuai dengan salah satu case tertentu, maka case tertentu itulah yang akan dijalankan
    #     case "posix": os.system("clear") # untuk linux dan mac
    #     case "nt": os.system("cls") # untuk windows

    CRUD.init_console()
    

    while(True):

        match sistem_operasi: # jika sistem_operasinya match/sesuai dengan salah satu case tertentu, maka case tertentu itulah yang akan dijalankan
            case "posix": os.system("clear") # untuk linux dan mac
            case "nt": os.system("cls") # untuk windows

        print("SELAMAT DATANG DI PROGRAM")
        print("DATABASE PERPUSTAKAAN")
        print("=========================")

        print(f'1. Read Data')
        print(f'2. Create Data')
        print(f'3. Update Data')
        print(f'4. Delete Data\n')

        user_option = input('Masukkan Opsi : ')

        match user_option: # jika user_option nya match/sesuai dengan salah satu case tertentu, maka case tertentu itulah yang akan dijalankan
            case "1": CRUD.read_console()
            case "2": CRUD.create_console()
            case "3": CRUD.update_console()
            case "4": CRUD.delete_console()

        is_done = input("Apakah Selesai (y/n)? ")

        if is_done == 'Y' or is_done == 'y':
            break

    print('Program Berakhir')




































































