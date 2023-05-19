import sqlite3
from sqlite3 import Error

def init_conn(path):
    conn = None
    try:
        conn = sqlite3.connect(path)
        print ("Connection established!")
    except Error as e:
        print (e)
        print ("Connection failed!")
    return conn

def init_tables(connection):
    sql = "CREATE TABLE IF NOT EXISTS Comedia(id integer PRIMARY KEY, name_film text NOT NULL);"
    connection.execute(sql)

def prepareDb(name):
    conn = init_conn(name)
    init_tables(conn)
    conn.close()

def getFilmsComedia(db):
    connection = init_conn(db)
    cursor = connection.cursor()
    cursor.execute('SELECT name_film FROM Comedia ORDER BY random() LIMIT 1')
    result = cursor.fetchall()
    text = str(result[0][0])
    connection.commit()
    connection.close()
    return text
