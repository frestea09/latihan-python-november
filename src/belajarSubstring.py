from __future__ import print_function

def main():
    kalimatPertama = 'ilman'
    kalimatKedua = input('Kalimat Kedua : ')
    print('Substring Pertama : %s'%kalimatPertama[0])
    print('Substring Pertama : %s'%kalimatPertama[:2])
    print('Substring Pertama : %s'%kalimatPertama[2:])
    print('Substring Pertama : %s'%kalimatPertama[2:5])
if __name__ == '__main__':
    main()