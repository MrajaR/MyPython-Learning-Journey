# 1. mode write 'w'

# jika menggunakan mode write maka harus ada argument encoding=utf-8
with open('part_35_Write External File\data_1.txt','w',encoding='utf-8') as file: # bisa menuliskan mode='w,r,a'(keyword argument), atau langsung saja mengisi valuenya (positional argument)
    file.write("hallo semuanya") # dengan begini otomatis akan membuat file data_1.txt jika belum ada, dan menambahkan isi dari file tsb dengan "hallo semuanya"

with open('part_35_Write External File\data_1.txt','w',encoding='utf-8') as file:
    file.write("hai teman-teman") # akan overwrite isi dari file sebelumnya

with open('part_35_Write External File\data_1.txt','w',encoding='utf-8') as file:
    file.write("di overwrite") # akan overwrite isi dari file sebelumnya


# 2. mode append 'a'
with open('part_35_Write External File\data_2.txt','w',encoding='utf-8') as file: # jika ini diganti dengan mode 'a' maka akan menambahkan secara terus menerus ketika code di run, ini tidak menambahkan terus menerus karena adanya mode write yang akan overwrite dan mereset isi dari filenya ketika code di run
    file.write("sydmen kontol\n") # membuat file data_2.txt dan mengisinya dengan 'sydmen kontol'

with open('part_35_Write External File\data_2.txt','a',encoding='utf-8') as file:
    file.write("sekiro\n") # "sekiro" akan ditambahkan ke file data_2.txt, tanpa mengoverwrite isi sebelumnya 

with open('part_35_Write External File\data_2.txt','a',encoding='utf-8') as file:
    file.write("tambah lagi dengan append") # "sekiro" akan ditambahkan ke file data_2.txt, tanpa mengoverwrite isi sebelumnya 

# 3. mode r+
# dengan mode r+ kita dapat read,append dan write file
# tapi read dan write tidak bisa disatukan dalam 1 statement with, jika disatukan tidak akan printout apa"
# ketika membuat statement with dengan file yang sama lalu kita write filenya dengan sesuatu -..
# maka akan menimpa isi sebelumnya sesuai panjang datanya (menimpa, bukan overwrite0)

with open('part_35_Write External File\data_3.txt','r+',encoding='utf-8') as file:
    file.write('ini data ke-3 nih\n') # write file, membuat file data_3.txt dan mengisinya (write pada baris pertama akan dianggap sebagai write yang overwrite dan write setelahnya akan mengappend)
    file.write('sydmen\n') # append file, menambahkan isi file
    file.write('sekiro prostetik\n') # append file, menambahkan isi file
    print(file.read()) # read file, akan tetapi tidak akan printout apa" karena digabung dengan write dalam 1 statement with

with open('part_35_Write External File\data_3.txt','r+',encoding='utf-8') as file:
    print(file.read()) # akan read file

with open('part_35_Write External File\data_3.txt','r+',encoding='utf-8') as file:
    file.write('nimpa nih cuy') # AKAN MENIMPA ISI TEXT SESUAI DENGAN PANJANG DATA

with open('part_35_Write External File\data_3.txt','r+',encoding='utf-8') as file:
    print(file.read()) # akan read file

## bukti bahwa dengan mode r+ dapat write dan read item
with open('part_35_Write External File\data_3.txt','r+',encoding='utf-8') as file:
    status_read = file.readable()
    status_write = file.writable()
    print(f'status read = {status_read}')
    print(f'status write = {status_write}')




















