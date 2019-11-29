from __future__ import print_function

def main():
    #menambahkan element kepada dictinary
    dictionarySaya = {1:'Satu',2:'Dua'}
    print('Sebelum Ditambah ')
    print(dictionarySaya)
    for element in dictionarySaya:
        print(dictionarySaya[element])
    dictionarySaya[3] = 'tiga'
    print(dictionarySaya)
if __name__ == '__main__':
    main()