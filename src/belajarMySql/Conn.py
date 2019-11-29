from __future__ import print_function
import mysql.connector
def main():
    conn = mysql.connector.connect(
        user="root",
        password="",
        host="localhost",
        database="baru"
    )
    curr = conn.cursor()
    ddl = '''
        CREATE TABLE buku(
            id CHAR(2) not null  primary key,
            judul varchar(50)
        )
    '''
    curr.execute(ddl)
    curr.close()
    conn.close()
if __name__ == '__main__':
    main()