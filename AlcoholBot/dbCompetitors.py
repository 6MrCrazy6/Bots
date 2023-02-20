import sqlite3
from sqlite3 import Error

def init_conn5(path):
    conn = None
    try:
        conn = sqlite3.connect(path)
        print ("Connection established!")
    except Error as e:
        print (e)
        print ("Connection failed!")
    return conn

def init_tables5(connection):
    sql = "CREATE TABLE IF NOT EXISTS competitors(id integer PRIMARY KEY, user_name text NOT NULL, beer integer NOT NULL);"
    connection.execute(sql)

def prepareDb5(name):
    conn = init_conn5(name)
    init_tables5(conn)
    conn.close()

def init_user5(db, name):
    sql = "SELECT * FROM competitors WHERE `user_name`='" + name + "';"
    connection = init_conn5(db)
    cursor = connection.cursor()
    connection.set_trace_callback(print)
    cursor.execute(sql)
    users = cursor.fetchall()
    usersAmount = len(users)
    if usersAmount == 0:
        sql = "INSERT INTO competitions(`user_name`, `beer`) VALUES('{}', 0);".format(name)
        cursor.execute(sql)
        connection.commit()
        connection.close()

