from __future__ import print_function
from abc import ABCMeta, abstractmethod

class AbstractHitung(metaclass=ABCMeta):
    @abstractmethod
    def tambah(self):
        pass
class Hitung(AbstractHitung):
    def __init__(self,bilanganPertama=None,bilanganKedua=None):
        self.__pertama = bilanganPertama
        self.__kedua = bilanganKedua
    def setPertama(self,var):
        self.__pertama = var
    def getPertama(self):
        return self.__pertama
    def setKedua(self,var):
        self.__kedua = var
    def getKedua(self):
        return self.__kedua
    def tambah(self):
        hasil = self.__pertama + self.__kedua
        return hasil
def main():
    bilanganPertama = 10
    bilanganKedua = 20
    myObj = Hitung()
    myObj.setPertama(bilanganPertama)
    myObj.setKedua(bilanganKedua)
    print(myObj.tambah())
if __name__ == '__main__':
    main()