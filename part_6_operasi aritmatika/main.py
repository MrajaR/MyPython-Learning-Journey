a = 10
b = 3

# operasi penambahan +
hasil = a + b
print(a, '+', b, '=', hasil)

# operasi pengurangan -
hasil = a - b
print(a, '-', b, '=', hasil)

#operasi perkalian *
hasil = a * b
print(a, '*', b, '=', hasil)

# operasi pembagian /
hasil = a / b
print(a, '/', b, '=', hasil)

# operasi eksponen (perpangkatan) **
hasil = a ** b
print(a, '**', b, '=', hasil)

# operasi modulus (sisa dari hasil pembagian yang bersisa) %
hasil = a % b
print(a, '%', b, '=', hasil) # jika habis dibagi, maka modulusnya bernilai 0

# operasi floor division (pembulatan ke bawah untuk setiap pembagian yang bersisa) //
hasil = a // b
print(a, '//', b, '=', hasil)

# prioritas operasi, operational precedence

"""
prioritas untuk operasi aritmatika :
1. ()
2. exponen **
3. perkalian,pembagian,modulus,floor division dan sejenisnya *,/,%,//
4. pertambahan dan pengurangan +-
"""

x = 3
y = 2
z = 4

hasil = x ** y * (z + x) / y - y % z // x
print(x,'**',y,'*',z,'+',x,'/',y,'-',y,'%',z,'//',x, '=', hasil)

hasil = (x + y) * z
print('(',x,'+',y,') *',z,'=',hasil)

hasil = x + y * z
print(x,'+',y,'*',z,'=',hasil)

