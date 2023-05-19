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
    sql = "CREATE TABLE IF NOT EXISTS Timer(id integer PRIMARY KEY, user_name text NOT NULL, start_time integer NOT NULL, end_time integer NOT NULL);"
    connection.execute(sql)

def prepareDb3(name):
    conn = init_conn(name)
    init_tables(conn)
    conn.close()

def init_user3(db, name):
    sql = "SELECT * FROM Timer WHERE `user_name`='" + name + "';"
    connection = init_conn(db)
    cursor = connection.cursor()
    connection.set_trace_callback(print)
    cursor.execute(sql)
    users = cursor.fetchall()
    usersAmount = len(users)
    if usersAmount == 0:
        sql = "INSERT INTO Timer(`user_name`,`start_time`,`end_time`) VALUES('{}', datetime('now'), datetime('now', '2 minutes'));".format(name)
        cursor.execute(sql)
        connection.commit()
        connection.close()

def getTime(db, name, type):
    sql = "SELECT {} FROM Timer WHERE `user_name`='{}';".format(type, name)
    connection = init_conn(db)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    if result == None:
        return result
    else:
        connection.commit()
        connection.close()
        return result[0]

def setTime(db, name, type, amount):
    sql = "UPDATE Timer SET `{}`={} WHERE `user_name`='{}';".format(type, amount, name)
    connection = init_conn(db)
    cursor = connection.cursor()
    cursor.execute(sql)
    connection.commit()
    connection.close()

def delTime(db, name):
    connection = init_conn(db)
    cursor = connection.cursor()
    cursor.execute('DELETE FROM Timer WHERE user_name = (?)', [name])
    connection.commit()
    connection.close()


