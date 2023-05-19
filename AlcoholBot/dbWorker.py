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
    sql = "CREATE TABLE IF NOT EXISTS AcloLitres(id integer PRIMARY KEY, user_name text NOT NULL, beer real NOT NULL, wine real NOT NULL, vodka real NOT NULL, whiskey real NOT NULL, cognac real NOT NULL, tequila real NOT NULL, " \
          "mulledwine real NOT NULL, sake real NOT NULL, mojito real NOT NULL, pinacolada real NOT NULL," \
          "cider real NOT NULL);"
    connection.execute(sql)

def prepareDb(name):
    conn = init_conn(name)
    init_tables(conn)
    conn.close()

def init_user(db, name):
    sql = "SELECT * FROM AcloLitres WHERE `user_name`='" + name + "';"
    connection = init_conn(db)
    cursor = connection.cursor()
    connection.set_trace_callback(print)
    cursor.execute(sql)
    users = cursor.fetchall()
    usersAmount = len(users)
    if usersAmount == 0:
        sql = "INSERT INTO AcloLitres(`user_name`, `beer`, `wine`, `vodka`, `whiskey`, `cognac`, `tequila`, `mulledwine`, `sake`, `mojito`, `pinacolada`, `cider`) VALUES('{}', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0);".format(name)
        cursor.execute(sql)
        connection.commit()
        connection.close()

def setLitres(db, name, type, amount):
    sql = "UPDATE AcloLitres SET `{}`={} WHERE `user_name`='{}';".format(type, amount, name)
    connection = init_conn(db)
    cursor = connection.cursor()
    cursor.execute(sql)
    connection.commit()
    connection.close()

def getLitres(db, name, type):
    sql = "SELECT {} FROM AcloLitres WHERE `user_name`='{}';".format(type, name)
    connection = init_conn(db)
    cursor = connection.cursor()
    cursor.execute(sql)
    items = cursor.fetchall()
    litres = int(items[0][0])
    connection.commit()
    connection.close()
    return litres

