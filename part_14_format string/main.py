0# format string (f)

nama = "ucup"
format_str = f"hello {nama}"
print(format_str)

# angka

angka = 2987.6
format_str = f"angka = {angka}"
print(format_str)

# boolean

tes_boolean = True
format_str = f"boolean = {tes_boolean}"
print(format_str)

# bilangan bulat
angka = 35
# d hanya untuk menandakan bahwa ini adalah bilangan bulat/int # tidak penting
format_str = f"bilangan bulat = {angka:d}"
print(format_str)

# bilangan ribuan
angka = 3500
# otomatis memberikan titik diantara ribuan/jutaan/ratusan dll
format_str = f"angka ribuan {angka:,}"
print(format_str)

angka = 487.36793
format_str = f"angka = {angka:.3f}"  # 3f brarti 3 angka dblakang koma
print(format_str)

# menampikan leading zero

angka = 487.36793
# 9 artinya angka akan ditempatkan dikanan dalam length 9, 
# dan sisa kosong di kiri akan diisi angka 0
format_str = f"angka = {angka:09.3f}"
print(format_str)


# menampilkan tanda + dan -
plus = 20.2345
plus_2 = 20
minus = -20
format_plus = f"angka plus = {plus:+.2f}" # + digunakan untuk menampilkan (+) dan 2f berarti mmunculkan 2 angka blakang koma
format_plus2 = f"angka plus kedua = {plus_2:+d}" # + untuk menampilkan (+) dan d menandai bahwa angkanya int
format_minus = f"angka minus = {minus}"

print(format_plus)
print(format_plus2)
print(format_minus)

# menampilkan percentage

persentase = 0.0875
format_persen = f"persentase = {persentase:.2%}" # 2 berarti dimunculkan 2 angka dibelakang koma
print(format_persen)

# melakukan operasi aritmatika dalam placeholder

harga = 250000
jumlah = 8

format_total = f"harga total = Rp.{harga*jumlah:,}"
print(format_total)

# format angka lain (binary, octal, hexadecimal)

angka = 235
format_binary = f"binary = {bin(angka)}"
format_octal = f"octal = {oct(angka)}"
format_hexa = f"hexadecimal = {hex(angka)}"

print(format_binary)
print(format_octal)
print(format_hexa)