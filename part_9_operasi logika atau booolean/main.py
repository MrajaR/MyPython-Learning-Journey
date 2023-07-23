# OPERASI LOGIKA ATAU BOOLEAN

# ADA NOT, OR, AND, XOR


print("====NOT")
a = True
c = not a
print('data boolean =', a)
print('data c =', c)


print("====OR") # jika ada satu saja nilai true maka die akan true
a = False
b = False
c = a or b
print(a, 'or', b, '=', c)
a = True
b = False
c = a or b
print(a, 'or', b, '=', c)
a = False
b = True
c = a or b
print(a, 'or', b, '=', c)
a = True
b = True
c = a or b
print(a, 'or', b, '=', c)

print("====and") # akan true jika semuanya true, bila ada 1 false saja maka akan false
a = False
b = False
c = a and b
print(a, 'and', b, '=', c)
a = True
b = False
c = a and b
print(a, 'and', b, '=', c)
a = False
b = True
c = a and b
print(a, 'and', b, '=', c)
a = True
b = True
c = a and b
print(a, 'and', b, '=', c)

print("====xor(^)") # akan true jika salah satu true, jika semua true/false makan akan false
a = False
b = False
c = a ^ b
print(a, 'xor', b, '=', c)
a = True
b = False
c = a ^ b
print(a, 'xor', b, '=', c)
a = False
b = True
c = a ^ b
print(a, 'xor', b, '=', c)
a = True
b = True
c = a ^ b
print(a, 'xor', b, '=', c)
