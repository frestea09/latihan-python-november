def main():
    bilanganPertama = 5
    bilanganKedua = 0
    try:
        hasil = bilanganPertama/bilanganKedua
    except (BaseException,Exception) as error:
        print(error)
    else:
        print(hasil)
if __name__ == '__main__':
    main()