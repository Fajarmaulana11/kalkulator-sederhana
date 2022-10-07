#Kalkulator Sederhana

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
    

#eksekusi

pilihan = 'y'
while pilihan == 'y':
    try:
        print(20*'=')
        print('KALKULATOR SEDERHANA')
        print(20*'=')
        
        a = int(input('masukan bilangan 1 = '))
        b = int(input('masukan bilangan 2 = '))
        print('\n1. Penjumlahan\n2. Pengurangan\n3. Perkalian\n4. Pembagian\n')
        c = input('\nPilih 1-4 = ')

        if c == '1':
            print('Hasil dari', a, '+', b, '=', tambah(a, b))
        elif c == '2':
            print('Hasil dari', a, '-', b, '=', kurang(a, b))
        elif c == '3':
            print('Hasil dari', a, 'x', b, '=', kali(a, b))
        elif c == '4':
            print('Hasil dari', a, '/', b, '=', bagi(a, b))
        elif c == '0':
            print('Jangan masukkan 0')
        else:
            print('Opsi yang anda pilih salah')
        pilihan = input("Mau Lagi ? [y/n] : ")
        if pilihan == 'n':
            print('PROGRAM SELESAI TERIMAKASIH')  
    except:
        print('Masukkan angka, bukan huruf')
