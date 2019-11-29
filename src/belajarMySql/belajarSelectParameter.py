from __future__ import print_function
import mysql.connector as mysql

def main():
    try:
        conn = mysql.connect(
            user='root',
            password='',
            host='localhost',
            database='baru'
        )
        curr = conn.cursor()
        sql = '''
            INSERT INTO hello VALUES(%s,%s)
        '''
        data = ('','lies lima')
        try:
            curr.execute(sql,data)
        except (BaseException,Exception) as error:
            conn.rollback()
            print(error)
        else:
            conn.commit()
            curr.close()
    except(BaseException,Exception) as error:
        print(error)
    else:
        conn.close()
        curr.close()
if __name__ == '__main__':
    main()