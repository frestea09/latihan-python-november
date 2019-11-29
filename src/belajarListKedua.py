from __future__ import print_function

def main():
    listSaya = [1,2,3,4,5,6]
    print('sebelum ditambah')
    print(listSaya)
    print('tambah')
    listSaya.append(7)
    print(listSaya)
    print('tambah')
    listSaya.insert(8,8)
    print(listSaya)
    print('tambah')
    listTambah = [10,11]
    listSaya.extend(listTambah)
    print(listSaya)
if __name__ == '__main__':
    main()
