import cx_Oracle

'''try:
    connection=cx_Oracle.connect(
    user = 'visitor',
    password = 'NiKolas1984*',
    dsn='localhost:1521/PruebaDjango'
    )
    
except Exception as err:
    print('Error en la conexion a la base de datos', err)
else:
    print(connection.version)

connection.close()
try:
    connection=cx_Oracle.connect(
    user='visitor',
    password='NiKolas1984*',
    dsn='localhost:1521/PruebaDjango'
    )
    
    print(connection.version)
except Exception as ex:
    print(ex)

connection.close()'''

connStr = 'visitor/NiKolas1984*@localhost:1521/PruebaDjango'

conn = cx_Oracle.connect(connStr)
cur = conn.cursor()

cur.close()
conn.close()
