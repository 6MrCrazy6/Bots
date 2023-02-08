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
    sql = "CREATE TABLE IF NOT EXISTS time(id integer PRIMARY KEY, user_name text NOT NULL, time integer NOT NULL);"
    connection.execute(sql)

def prepareDb3(name):
    conn = init_conn(name)
    init_tables(conn)
    conn.close()

def init_user3(db, name):
    sql = "SELECT * FROM time WHERE `user_name`='" + name + "';"
    connection = init_conn(db)
    cursor = connection.cursor()
    connection.set_trace_callback(print)
    cursor.execute(sql)
    users = cursor.fetchall()
    usersAmount = len(users)
    if usersAmount == 0:
        sql = "INSERT INTO time(`user_name`,`time`) VALUES('{}', time('now'));".format(name)
        cursor.execute(sql)
        connection.commit()
        connection.close()

def setTime(db, name, type, time):
    sql = "UPDATE time SET `time`=time('now') WHERE `user_name`='{}';".format(type, name, time)
    connection = init_conn(db)
    cursor = connection.cursor()
    cursor.execute(sql)
    connection.commit()
    connection.close()


def delTime(db, name, type):
    sql = "DELETE {} FROM time WHERE `user_name`='{}';".format(type, name)
    connection = init_conn(db)
    cursor = connection.cursor()
    cursor.execute(sql)
    connection.commit()
    connection.close()

