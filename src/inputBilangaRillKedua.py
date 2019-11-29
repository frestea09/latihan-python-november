from __future__ import print_function

def main():
    bilanganRillPertama = float(input('Bilangan Pertama : '))
    bilanganRillKedua = float(input('Bilangan Kedua : '))
    hasil = bilanganRillPertama * bilanganRillKedua
    print('Bilangan Pertama : %.2f dan bilangan Kedua : %.2f'%(bilanganRillPertama,bilanganRillKedua))
    print('hasil : %.2f'%hasil)
if __name__ == '__main__':
    main()