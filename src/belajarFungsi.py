from __future__ import print_function
def helloWorld():
    print('Hello World')
def tambah(inputBilanganPertama, inputBilanganKedua):
    hasil = inputBilanganPertama + inputBilanganKedua
    return hasil
def length(*var):
    print(var)
    for element in var:
        print(element)
def main():
    bilanganPertama = int(input('Bilangan Pertama : '))
    bilanganKedua = int(input('Bilangan kedua'))
    hasil = tambah(bilanganPertama,bilanganKedua)
    length(bilanganKedua)
if __name__ == '__main__':
    main()