# operasi yang dilakukan dengan penulisan assignment yg lebih singkat
a = 5 # adalah assignment
print("nilai a =",a)

a = a + 1
print("nilai a =",a)

a += 1 # artinya adalah a = a + 1
print("nilai a =",a)

a -= 2 # artinya adalah a = a - 2
print("nilai a =",a)

a *= 5 # artinya adalah a = a * 5
print("nilai a =",a)

a /= 5 # artinya adalah a = a / 5
print("nilai a =",a)

a /= 5 # artinya adalah a = a / 5
print("nilai a =",a)


# floor division dan modulus
b = 10
print('nilai b =',b) 

b %= 3
print('nilai b =',b) # artinya adalah b = b % 3

b = 10
print('nilai b =',b)

b //= 3
print('nilai b =',b) # artinya adalah b = b // 3

# perpangkatan/eksponen

a = 5
print('nilai a = ',a)

a **= 3
print('nilai a =', a)

# operasi bitwise
# or
c = True
print("\nnilai c =", c)
c |= False
print("nilai c |= false, menjadi", c)
c = False
print("\nnilai c =", c)
c |= False
print("nilai c |= false, , menjadi", c)

# and
c = True
print("\nnilai c =", c)
c &= False
print("nilai c &= false, menjadi", c)
c = True
print("\nnilai c =", c)
c &= True
print("nilai c &= true, , menjadi", c)

#xor
c = True
print("\nnilai c =", c)
c ^= False
print("nilai c ^= false, menjadi", c)
c = True
print("\nnilai c =", c)
c ^= True
print("nilai c ^= true, , menjadi", c)

# geser geser
d = 0b0100
print('nilai d =',format(d,"05b"))
d >>= 2
print("nilai d >>= 2 , menjadi =", format(d,'04b'))
d <<= 1
print("nilai d <<= 1 , menjadi =", format(d,'04b'))





