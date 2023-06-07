import mysql.connector
from mysql.connector import errorcode

def connect():
    """ Connect to MySQL database """
    conn = None
    try:
        conn = mysql.connector.connect(dsn='pruebadjango_high',
                                       user = 'visitor',
                                        password = 'NiKolas1984*')
        if conn.is_connected():
            print('Connected to MySQL database')

    except Error as e:
        print(e)

    finally:
        if conn is not None and conn.is_connected():
            conn.close()


if __name__ == '__main__':
    connect()