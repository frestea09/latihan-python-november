from __future__ import print_function

def main():
    fileSaya = open('data.txt','r+')
    data = fileSaya.readlines()
    for element in data:
        print(element)
    fileSaya.close()
if __name__ == '__main__':
    main()