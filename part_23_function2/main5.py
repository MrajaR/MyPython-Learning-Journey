### anonymous function

def fungsi_pangkat(n):
    return lambda angka:angka**n

pangkat2 = fungsi_pangkat(2) # menginput angka 2 untuk argument 'n' yakni pangkatnya
print(f'hasil pangkat 2 = {pangkat2(3)}') # menginput angka 3 untuk argument 'angka' yakni bilangan yang ingin dipangkatkan

pangkat3 = fungsi_pangkat(3)# menginput angka 3 untuk argument 'n' yakni pangkatnya
print(f'hasil pangkat 3 = {pangkat3(9)}') # menginput angka 9 untuk argument 'angka' yakni bilangan yang ingin dipangkatkan

# bisa juga seperti ini
print(f'hasil pangkat dari anonymous function bebas = {fungsi_pangkat(4)(2)}') # 4 adalah input untuk argument "n" dan 2 adalah input untuk argument "angka"

