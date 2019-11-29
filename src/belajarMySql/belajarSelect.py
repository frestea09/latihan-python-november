from __future__ import print_function
import mysql.connector as mysql

def main():
    try:
        conn = mysql.connect(
            user = 'root',
            password = '',
            host = 'localhost',
            database = 'baru'
        )
        curr = conn.cursor()
        sql = '''
            SELECT * FROM hello
        '''
        curr.execute(sql)
        result =  curr.fetchall()
        for element in result:
            id = element[0]
            nama = element[1]
            print(id,'\t',nama,'\t')
    except (BaseException,Exception) as error:
        print(error)
    else:
        curr.close()
        conn.close()
if __name__ == '__main__':
    main()