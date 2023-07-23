

def menghitung_kecepatan():
    print(5*"=" + "menghitung kecepatan" + 5*"=")
    waktu = float(input("masukkan waktu : "))
    jarak = float(input("masukkan jarak : "))
    velocity = jarak/waktu
    print(f"kecepatan = {velocity}")

def luas_segitiga():
    print(5*"=" + "menghitung luas segitiga" + 5*"=")
    alas = float(input("masukkan panjang alas : "))
    tinggi = float(input("masukkan tinggi : "))
    luas_segitiga = 0.5 * alas * tinggi
    print(f"luas segitiga = {luas_segitiga}")

def volume_bola():
    print(5*"=" + "menghitung volume bola" + 5*"=")
    r = float(input("masukkan panjang jari-jari : "))
    volume_bola = 4/3 * 3.14 * (r**3) 
    print(f"volume bola = {volume_bola}")

def luas_balok():
    print(5*"=" + "menghitung luas permukaan balok" + 5*"=")
    lebar = float(input("masukkan lebar : "))
    tinggi = float(input("masukkan tinggi : "))
    panjang = float(input("masukkan panjang : "))
    luas_balok = (2*panjang*lebar) + (2*panjang*tinggi) + (2*tinggi*lebar)
    print(f"luas permukaan balok = {luas_balok}")

while True:
    userInput = float(input("""
    pilih rumus yang akan dipakai :

    1. rumus kecepatan 
    2. rumus luas segitiga 
    3. rumus volume bola 
    4. rumus volume balok
    
    0.keluar program
    
    pilih nomor berapa :"""))
    if userInput == 1 :
        menghitung_kecepatan()
    elif userInput == 2 :
        luas_segitiga()
    elif userInput == 3:
        volume_bola()
    elif userInput == 4 :
        luas_balok()
    else:
        break