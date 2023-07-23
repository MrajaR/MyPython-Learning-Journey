def tambah(*args):
    hasil = 0
    for x in args:
        hasil += x
    
    return hasil

def kali(*args):
    hasil = 1
    for x in args:
        hasil *= x

    return hasil

def pangkat(n):
    return lambda angka:angka ** n
    