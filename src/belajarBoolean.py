from __future__ import print_function

def main():
    threshold = True
    bilanganPertama = int(input('Bilangan Pertama : '))
    bilanganKedua = int(input('Bilangan Kedua : '))
    hasil = bilanganPertama + bilanganKedua
    status = 'genap'
    if(hasil % 2 == 0):
        threshold = False
    if(threshold):
        status = 'ganjil'
    print('Status : %s'%status)
if __name__ == '__main__':
    main()