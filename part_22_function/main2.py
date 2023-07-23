### fungsi dengan return(kembalian)

## sebenarnya fungsi dalam pemrograman diambil dari konsep y = f(x)
## akan tetapi di pemrograman didefiniskan dengan lebih jelas dan literal
## 'f(x)='  sama dengan 'def nama_fungsi:'
## badan fungsinya adalah isi bagaimana proses pengolahan x dalam f(x)
## y = return

## contoh fungsi kuadrat dengan return

def kuadrat(input_x): # f(x)
    output_y = input_x**2 # proses pengolahan x dalam f(x)
    return output_y # y

# jika begini maka akan eror, karena tidak diinput argumentnya
# print(kuadrat())

## memanggil function ini dgn cara seperti ini tidak akan memunculkan output apapun
## karena function ini tidak berisikan print(), tapi hanya return yang mana mesti panggil dgn cara diprint
## atau dengan cara mempassingnya ke sebuah variabel dan memprint variabel tsb
# kuadrat(2)

y = kuadrat(3)
print(y)

print(kuadrat(7))

z = 100 + kuadrat(5)
print(z)