from __future__ import print_function

def main():
    inputKalimatPertama = input('Kalimat Pertama : ')
    inputKalimatKedua = input('Kalimat Kedua : ')
    hasil = 'Kalimat berbeda'
    if(inputKalimatPertama == inputKalimatKedua):
        hasil = 'Kalimat Sama'
    print('Kalimat Pertama : %s \n Kalimat Kedua : %s \n hasil : %s'%(inputKalimatPertama,inputKalimatKedua,hasil))
if __name__ == '__main__':
    main()