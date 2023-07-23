# json adalah data exchange format, ketika file dalam format json maka akan bisa dibuka dan diolah dari satu bahasa ke bahasa lain

book = {}

book['sydmen'] = {
    'name':'sydmen',
    'umur':22,
    'hobi':'gymrat'
}

book['markus'] = {
    'name':'markus',
    'umur':17,
    'hobi':'sekiro'
}

for key,value in book.items():
    print(f'key = {key}, value = {value}')

import json

s = json.dumps(book)
print(f'json = {s}') # convert dict ke string dan dari string ke json
print(type(s)) # typenya string

with open(r'part_36_handling json file\book.txt','w') as f: # book.txt bentuknya adalah json
    f.write(s)

with open(r'part_36_handling json file\book.txt','r') as f:
    s = f.read()
    print(s) # bentuknya string
    print(type(s))

book = json.loads(s) # merubah ke bentuk dict
print(book)
print(type(book))

# setelah json diconvert ke bentuk dict di python, maka baru bisa diolah
print(book['sydmen']['umur'])

for person in book:
    print(book[person])


























