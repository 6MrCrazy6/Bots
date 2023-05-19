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
    sql = "CREATE TABLE IF NOT EXISTS DataBase(id integer PRIMARY KEY, question text NOT NULL, answer text NOT NULL);"
    connection.execute(sql)

def prepareDb1(name):
    conn = init_conn(name)
    init_tables(conn)
    conn.close()

def getAnswer(db, name, type):
    sql = "SELECT {} FROM DataBase WHERE `question`='{}';".format(type, name)
    connection = init_conn(db)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)
    if result == []:
        return result
    else:
        answer = str(result[0][0])
        connection.commit()
        connection.close()
        return answer

def addAnswer(db, name):
    sql = "INSERT INTO DataBase(`question`, `answer`) VALUES('{}', ' ');".format(name)
    connection = init_conn(db)
    cursor = connection.cursor()
    cursor.execute(sql)
    connection.commit()
    connection.close()

def setAnswer(db, name):
    sql = "UPDATE DataBase SET `answer`='{}' WHERE `answer`= ' ';".format(name)
    connection = init_conn(db)
    cursor = connection.cursor()
    cursor.execute(sql)
    connection.commit()
    connection.close()
