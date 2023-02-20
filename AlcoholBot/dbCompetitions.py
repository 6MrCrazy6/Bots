import sqlite3
from sqlite3 import Error

def init_conn4(path):
    conn = None
    try:
        conn = sqlite3.connect(path)
        print ("Connection established!")
    except Error as e:
        print (e)
        print ("Connection failed!")
    return conn

def init_tables4(connection):
    sql = "CREATE TABLE IF NOT EXISTS competitions(id integer PRIMARY KEY, name_table text NOT NULL, end_time integer NOT NULL, status_table text NOT NULL);"
    connection.execute(sql)

def prepareDb4(name):
    conn = init_conn4(name)
    init_tables4(conn)
    conn.close()

def init_user4(db, name):
    sql = "SELECT * FROM competitions WHERE `name_table`='" + name + "';"
    connection = init_conn4(db)
    cursor = connection.cursor()
    connection.set_trace_callback(print)
    cursor.execute(sql)
    users = cursor.fetchall()
    usersAmount = len(users)
    if usersAmount == 0:
        sql = "INSERT INTO competitions(`name_table`, `end_time`, `status_table`) VALUES('{}', 0, 'Соревнования продолжаются');".format(name)
        cursor.execute(sql)
        connection.commit()
        connection.close()

def setTime(db, time, type):
    sql = "UPDATE competitions SET `end_time`=datetime('now') WHERE `end_time`='0';".format(type, time)
    connection = init_conn4(db)
    cursor = connection.cursor()
    cursor.execute(sql)
    connection.commit()
    connection.close()

def setStatus(db, time, type):
    sql = "UPDATE competitions SET `status_table`= 'Стол был остановлен' WHERE `status_table`='Соревнования продолжаются';".format(type, time)
    connection = init_conn4(db)
    cursor = connection.cursor()
    cursor.execute(sql)
    connection.commit()
    connection.close()