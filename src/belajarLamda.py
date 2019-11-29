from __future__ import print_function

def main():
    iniLamda = lambda x,y: x*y
    bilanganPertama = int(input('Bilangan Pertama : '))
    bilanganKedua = int(input('Bilangan Kedua : '))
    print('Bilangan Pertama : %d'%bilanganPertama)
    print('Bilangan Kedua : %d'%bilanganKedua)
    print('Hasil : %d'%iniLamda(bilanganPertama,bilanganKedua))
if __name__ == '__main__':
    main()