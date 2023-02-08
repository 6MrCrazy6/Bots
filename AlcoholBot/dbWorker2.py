import sqlite3
from sqlite3 import Error

def init_conn1(path):
    conn = None
    try:
        conn = sqlite3.connect(path)
        print ("Connection established!")
    except Error as e:
        print (e)
        print ("Connection failed!")
    return conn

def init_tables1(connection):
    sql = "CREATE TABLE IF NOT EXISTS users2(id integer PRIMARY KEY, user_name text NOT NULL, tea real NOT NULL, coffe real NOT NULL, " \
          "cocacola real NOT NULL, bubbletea real NOT NULL, fruitdrink real NOT NULL, milkshake real NOT NULL, sprite real NOT NULL, fanta real NOT NULL," \
          "nonalcoholicbeer real NOT NULL, nonalcoholicmojito real NOT NULL);"
    connection.execute(sql)

def prepareDb2(name):
    conn = init_conn1(name)
    init_tables1(conn)
    conn.close()

def init_user1(db, name):
    sql = "SELECT * FROM users2 WHERE `user_name`='" + name + "';"
    connection = init_conn1(db)
    cursor = connection.cursor()
    connection.set_trace_callback(print)
    cursor.execute(sql)
    users = cursor.fetchall()
    usersAmount = len(users)
    if usersAmount == 0:
        sql = "INSERT INTO users2(`user_name`, `tea`, `coffe`, `cocacola`, `bubbletea`, `fruitdrink`, `milkshake`, `sprite`, `fanta`, `nonalcoholicbeer`, `nonalcoholicmojito`) VALUES('{}', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0);".format(name)
        cursor.execute(sql)
        connection.commit()
        connection.close()

def setLitres2(db, name, type, amount):
    sql = "UPDATE users2 SET `{}`={} WHERE `user_name`='{}';".format(type, amount, name)
    connection = init_conn1(db)
    cursor = connection.cursor()
    cursor.execute(sql)
    connection.commit()
    connection.close()

def getLitres2(db, name, type):
    sql = "SELECT {} FROM users2 WHERE `user_name`='{}';".format(type, name)
    connection = init_conn1(db)
    cursor = connection.cursor()
    cursor.execute(sql)
    items = cursor.fetchall()
    litres = int(items[0][0])
    connection.commit()
    connection.close()
    return litres