import datetime as dt

print("silahkan masukkan tanggal, bulan tahun lahir anda\n")
tahun = int(input("masukkan tahun \t\t : "))
tanggal = int(input("masukkan tanggal \t : "))
bulan = int(input("masukkan bulan \t\t : "))

tanggal_lahir = dt.date(tahun, bulan, tanggal)

print('\n' + 5*'=' + "hasil" + 5*'=')
hari_ini = dt.date.today()
print(f"hari ini = {hari_ini}")
umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365
umur_bulan_sisa = (umur_hari.days % 365) // 30

print(f"tanggal lahir anda adalah {tanggal_lahir}")
print(f"hari lahir anda adalah {tanggal_lahir:%A}")
print(f"umur hari mu adalah {umur_hari.days} hari")
print(f"umur tahun mu adalah {umur_tahun} tahun, {umur_bulan_sisa} bulan")

