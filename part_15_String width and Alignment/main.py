# width and multiline

data_nama = "raja"
data_umur = 21
data_tinggi = 182.5
data_nomor_sepatu = 44

"""
note: dengan menggunakan 
key "f" pada string, data type selain string pada string
akan langsung tercasting menjadi string dengan
menggunakan "{}" kemudian memasukkan nama variabel ke dalamnya
dan untuk menyambungnya dengan string/variabel lain 
tidak diperlukan lagi "+".
"""

# string standard

data_lengkap = f"nama = {data_nama}, umur = {data_umur} tahun,  tinggi badan = {data_tinggi} cm, nomor sepatu = {data_nomor_sepatu}"
print(5*"=" + "data string" + 5*"=")
print(data_lengkap)

# string multiline (menggunakan \n)

data_lengkap = f"nama = {data_nama}, \numur = {data_umur} tahun,  \ntinggi badan = {data_tinggi} cm, \nnomor sepatu = {data_nomor_sepatu}"
print("\n"+5*"=" + "data string" + 5*"=")
print(data_lengkap)

# string multiline (menggunakan kutip triplets)

data_lengkap = f"""
nama = {data_nama}
umur = {data_umur}
tinggi badan = {data_tinggi}
nomor sepatu = {data_nomor_sepatu}
"""
print(5*"=" + "data string" + 5*"=")
print(data_lengkap)

# mengatur lebar/width

data_lengkap = f"""
nama         = {data_nama:>5}
umur         = {data_umur:>5}
tinggi badan = {data_tinggi:>5}
nomor sepatu = {data_nomor_sepatu:<5}
"""
print(5*"=" + "data string" + 5*"=")
print(data_lengkap)

