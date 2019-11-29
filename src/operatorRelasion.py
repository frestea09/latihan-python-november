from __future__ import print_function

def main():
    bilanganPertama = 5
    bilanganKedua = 4
    listSaya = [1,2,3,4,5]
    if(bilanganPertama == bilanganKedua):
        print('Bilangan Sama ')
    if(bilanganPertama >= bilanganKedua):
        print('Bilangan pertama lebih besar ')
    if(bilanganPertama <= bilanganKedua):
        print('Bilangan pertama lebih Kecil ')
    if(bilanganPertama != bilanganKedua):
        print('Bilangan pertama dan Kedua berbeda ')
    if(bilanganPertama in listSaya):
        print('Bilangan pertama ada pada list ')
if __name__ == '__main__':
    main()