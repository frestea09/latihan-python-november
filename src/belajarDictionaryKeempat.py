from __future__ import print_function

def main():
    dictonarySatu = {1:'Satu','gagal':'gagal',3:'Tiga',4:'empat'}
    print('Sebelum didelete')
    print(dictonarySatu)
    del dictonarySatu['gagal']
    print('Setelah Didelete')
    print(dictonarySatu)
if __name__ == '__main__':
    main()