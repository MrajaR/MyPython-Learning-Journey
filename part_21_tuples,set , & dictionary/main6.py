### multi keys & nesting dictionary
import datetime

mahasiswa1 = {
    'nama':'syanda',
    'nim':'2002055040',
    'sks_lulus':130,
    'beasiswa':False,
    'lahir': datetime.datetime(1999,10,29)
}

mahasiswa2 = {
    'nama':'markus',
    'nim':'2002055041',
    'sks_lulus':140,
    'beasiswa':False,
    'lahir': datetime.datetime(2004,3,20)
}
mahasiswa3 = {
    'nama':'Raja',
    'nim':'2002055042',
    'sks_lulus':140,
    'beasiswa':True,
    'lahir': datetime.datetime(2001,8,15)
}

data_mahasiswa = {
    'MAH001': mahasiswa1,
    'MAH002': mahasiswa2,
    'MAH003': mahasiswa3
}

print(f"{'KEY':<8} {'Nama':^17} {'NIM':^8} {'SKS':^10} {'Beasiswa':^9} {'Lahir':^10}")
print('-'*50)

for mahasiswa in data_mahasiswa:

    KEY = mahasiswa
    
    NAMA = data_mahasiswa[mahasiswa]['nama']
    NIM = data_mahasiswa[mahasiswa]['nim']  
    SKS = data_mahasiswa[mahasiswa]['sks_lulus'] 
    BEASISWA = data_mahasiswa[mahasiswa]['beasiswa']
    LAHIR = data_mahasiswa[mahasiswa]['lahir'].strftime("%x")
   

    print(f'{KEY:<8} {NAMA:^17} {NIM:^8} {SKS:^10} {BEASISWA:^9} {LAHIR:^10}')