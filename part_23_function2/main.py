### penggunaan type hints di function (petunjuk keterangan)

## berikut alasan digunakannya type hints di python
'''
def fungsi(argument):
    hasil = argument**2
    print(hasil)

fungsi(1) # akan mengeluarkan output tanpa adanya error
fungsi('syd') # output akan error, akan tetapi di display text editor tidak ada tanda-tanda error
fungsi(True) # output akan error, akan tetapi di display text editor tidak ada tanda-tanda error
'''
\
# berikut contoh penggunaan hints
# hints tidak berpengaruh apa-apa pada output, hints hanya memberikan keterangan di display text editor
# argument:int, artinya input utk argumentnya mesti int
# -> int, artinya function memiliki return yang bernilai int
def pangkat(argument:int) -> int:
    output = argument**2
    return output

print(pangkat(7))
# print(pangkat('syd')) # tidak akan ada tanda-tanda error, tetapi setelah di run baru ketahuan error

# contoh fungsi yang mereturn/beroutput integer namun diberi hints str untuk input dan returnnya
# hintsnya tidak berpengaruh pada outputnya, output tetap integer
# hints hanya memberikan keterangan di display text editor (saat mouse dihover ke arah fungsi tsb)
'''
def sepuluh_pangkat(argument:str) -> str:
    hasil = 10**argument
    return hasil

print(sepuluh_pangkat('syd'))
'''

# jika hints utk argumentnya sudah benar maka hints untuk returnya otomatis benar
def tes(argument:str):
    a = 'syd '
    return a + argument

print(tes('haii'))

# munculnya hints benar-benar terserah apa yang kita ingin tuliskan sebagai hints (int,float,bool,str)
# bahkan function yang tidak punya return pun dapat ditambahkan hints return (TAPI TIDAK BERPENGARUH PADA OUTPUT PROGRAM)
def say_hi(argument) -> int: # hints yang ngaco, karena function tidak punya return
    print(argument)

say_hi('sydmen')

