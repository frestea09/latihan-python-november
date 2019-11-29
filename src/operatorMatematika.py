from __future__ import print_function

def main():
    bilanganPertama = int(input('Bilangan Pertama : '))
    bilanganKedua = int(input('Bilangan Kedua : '))
    hasilTambah = bilanganPertama + bilanganKedua
    hasilKurang = bilanganPertama - bilanganKedua
    hasilKali = bilanganPertama * bilanganKedua
    hasilBagi = bilanganPertama / bilanganKedua
    hasilPangkat = bilanganPertama ** bilanganKedua
    hasilModulus = bilanganPertama % bilanganKedua
    print('Hasil Tambah : %d'%hasilTambah)
    print('Hasil Tambah : %d'%hasilKurang)
    print('Hasil Tambah : %d'%hasilKali)
    print('Hasil Tambah : %d'%hasilBagi)
    print('Hasil Tambah : %d'%hasilPangkat)
    print('Hasil Tambah : %d'%hasilModulus)
if __name__ == '__main__':
    main()