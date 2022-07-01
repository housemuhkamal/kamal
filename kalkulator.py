def tambah(a, b):
    tambah = float(a) + float(b)
    return tambah

def kurang(a, b):
    kurang = float(a) - float(b)
    return kurang

def kali(a, b):
    kali = float(a) * float(b)
    return kali

def bagi(a, b):
    bagi = float(a) / float(b)
    return bagi

while True:
    print('n\n\t\t=============kalkilator milik kamal=============\n\n')
    a = input('masukan bilangan 1: ')
    b = input('masukan bilangan 2: ')
    print('\n1. penjumlahan \n2. pengurangan \n3. perkalian \n4. pembagian \n5. batal')
    c = input('\npilih 1-5: ')
    if c == '1':
        print('hasilnya adalah: ', tambah(a, b))
    elif c == '2':
         print('hasilnya adalah: ', kurang(a, b))
    elif c == '3':
         print('hasilnya adalah: ', kali(a, b))
    elif c == '4':
         print('hasilnya adalah: ', bagi(a, b))
    elif c == '5':
         break
    else :
        print('operasi tidak di temukan')
