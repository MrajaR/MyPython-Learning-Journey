# infinite loop
# angka = 8

# while angka > 5:
#     print("this is infinity")

angka = 0
print(f"angka sekarang -> {angka}")

while angka < 5:
    print(angka)
    angka += 1

print('====contoh====')
angka = 0
print(f"angka sekarang -> {angka} \n")

while angka < 5: # akan terus loop jika memenuhi kondisi kurang dari lima (true), dan loop akan berhenti ketika angka = 5
    angka += 1 # statement yang membatasi loop (angka bertambah satu setiap terjadi pengulangan)
    print("tes finite loop", angka) # loop ini akan berhenti ketika angka sudah menjadi 5

print('====contoh 2====')
angka = 0

while angka <= 5: # akan berhenti ketika angka = 6
    angka += 1
    print('angka sekarang =', angka) # dari output ini diketahui bahwa angka bertambah 1 setiap kali perulangan
    print("tes finite loop")

tes = ['kayumanis','pisangan','utankayu','tebet','rawamangun']
print(len(tes))
i = 0
while i < len(tes):
    print('nama daerah =', tes[i])
    i += 1
    