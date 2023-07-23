# operasi komparasi
# hasil dari operasi komparasi adalah data boolean

# operasi komparasi menggunakan simbol : <, >, =<, =>, ==, !=, is, is not

a = 4
b = 2

# lebih besar dari >
print("===lebih besar dari===")
hasil = a > 3
print(a,'>',3,"=", hasil)
hasil = b > 3
print(b,'>',3,"=", hasil)
hasil = b > 2
print(b,'>',2,"=", hasil)

# lebih kurang dari <
print("===lebih kurang dari===")
hasil = a < 3
print(a,'<',3,"=", hasil)
hasil = b < 3
print(b,'<',3,"=", hasil)
hasil = b < 2
print(b,'<',2,"=", hasil)

# lebih dari sama dengan >=
print("===lebih dari sama dengan===")
hasil = a >= 3
print(a,'>=',3,"=", hasil)
hasil = b >= 3
print(b,'>=',3,"=", hasil)
hasil = b >= 2
print(b,'>=',2,"=", hasil)

# kurang dari sama dengan <=
print("===kurang dari sama dengan===")
hasil = a <= 3
print(a,'<=',3,"=", hasil)
hasil = b <= 3
print(b,'<=',3,"=", hasil)
hasil = b <= 2
print(b,'<=',2,"=", hasil)

# sama dengan == 
print("===sama dengan===")
hasil = a == 3
print(a,'==',3,"=", hasil)
hasil = b == 3
print(b,'==',3,"=", hasil)
hasil = b == 2
print(b,'==',2,"=", hasil) #sama dengannya dobel (==) karena untuk komparasi, jika hanya satu (=) maka itu assignment

# tidak sama dengan != 
print("===tidak sama dengan===")
hasil = a != 3
print(a,'!=',3,"=", hasil)
hasil = b != 3
print(b,'!=',3,"=", hasil)
hasil = b != 2
print(b,'!=',2,"=", hasil)

# is/is not, sebagai komparasi object identity
print('==is/is not, sebagai komparasi object identity==')
x = 5
y = 5
print(id(x))
print('nilai x =',x, 'id = ', hex(id(x)))
print('nilai y =',y, 'id = ', hex(id(y)))

hasil = x is not y
print(hasil)

x = 5
y = 5
print('nilai x =',x, 'id = ', hex(id(x)))
print('nilai y =',y, 'id = ', hex(id(y)))

hasil = x is y
print(hasil)

x = 5
y = 6
print('nilai x =',x, 'id = ', hex(id(x)))
print('nilai y =',y, 'id = ', hex(id(y)))

hasil = x is y
print(hasil)
