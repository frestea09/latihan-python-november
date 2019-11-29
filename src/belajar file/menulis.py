from __future__ import print_function

def main():
    fileSaya = open('data.txt','w+')
    dataTulis = 'ilman teguh prasetya'
    fileSaya.write(dataTulis)
    fileSaya.close()
if __name__ == '__main__':
    main()