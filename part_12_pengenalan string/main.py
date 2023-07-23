
data = "ini adalah string"
print(data)
print(type(data))

# cara membuat string
'''
1. menggunakan single quote '...'
2. menggunakan double quote "..."
'''

data = 'string dengan single quote'
print(data)

data = 'string dengan double quote'
print(data)

print('"Halo, apa kabar?"')
print("'Halo, apa kabar?'")
print("ini adalah hari jum'at")

# 2.menggunakan tanda \

# membuat tanda ' menjadi string
print('ini adalah hari jum\'at')
print('g\'day, isn\'it?')

#backslash

print("C:\\user\\Ucup")

# tab

print("ucup\totong")

# backspace
print("ucup\botong")

# newline
print("baris pertama\nbaris kedua")

# 3. string literal atau raw

#raw string

print(r"C:\new folder") # tanda tanda sperti backslash dkk tidak akan terdetect dgn simbol "r"

# multiline literal string

print("""
Nama: Raja
prodi: ekis
nim: 2002055040
""")

# multiline literal string dan raw


print(r"""
Nama: Raja
prodi: ekis
nim: 2002055040
website: www.ucup.com\newId
""")