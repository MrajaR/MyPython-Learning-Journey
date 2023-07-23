# latihan konversi satuan temperature

# program celcius ke satuan lain 

print("\nPROGRAM KONVERSI CELCIUS\n")
celcius = float(input("masukkan suhu dalam celcius: "))
print("suhu adalah", celcius, "derajat celcius")

reamur = celcius * 4/5
print("\ndalam reamur bernilai", reamur, "derajat reamur")

fahrenheit = celcius * 9/5 + 32
print("\ndalam fahrenheit bernilai", fahrenheit, "derajat fahrenheit" )

kelvin = celcius + 273
print("\ndalam kelvin bernilai", kelvin, "derajat kelvin" )

# program reamur ke satuan lain
print("\n=======perhitungan reamur ke satuan lain=========\n")

reamur = float(input("masukkan suhu dalam reamur: "))
print("suhu adalah", reamur, "derajat reamur")

celcius = reamur * 5/4
print("\ndalam celcius bernilai", celcius, "derajat celcius")

fahrenheit = reamur * 9/4 + 32
print("\ndalam fahrenheit bernilai", fahrenheit, "derajat fahrenheit" )

kelvin = celcius + 273
print("\ndalam kelvin bernilai", kelvin, "derajat kelvin" )

# program fahrenheit ke satuan lain
print("\n=======perhitungan reamur ke satuan lain=========\n")

fahrenheit = float(input("masukkan suhu dalam fahrenheit: "))
print("suhu adalah", fahrenheit, "derajat fahrenheit")

celcius = 5/9 * (fahrenheit - 32)
print("\ndalam celcius bernilai", celcius, "derajat celcius")

reamur = 4/9 * (fahrenheit - 32)
print("\ndalam reamur bernilai", reamur, "derajat reamur" )

kelvin = celcius + 273
print("\ndalam kelvin bernilai", kelvin, "derajat kelvin" )

# program kelvin ke satuan lain
print("\n=======perhitungan kelvin ke satuan lain=========\n")

kelvin = float(input("masukkan suhu dalam kelvin: "))
print("suhu adalah", kelvin, "derajat kelvin")

celcius = kelvin - 273
print("\ndalam celcius bernilai", celcius, "derajat celcius")

fahrenheit = celcius * 9/5 + 32
print("\ndalam fahrenheit bernilai", fahrenheit, "derajat fahrenheit" )

reamur = celcius * 4/5
print("\ndalam reamur bernilai", reamur, "derajat reamur" )







