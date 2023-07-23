# MODULE MATEMATIKA

def tambah(*args):
    output = 0

    for x in args:
        output += x

    return output

def kali(*args):
    output = 1

    for x in args:
        output *= x

    return output

def pangkat(eksponen:int):
    return lambda angka:angka**eksponen