

import mysql.connector
from mysql.connector import errorcode

DB_NAME = 'Amazon_Parse_Bugs'

TABLES = {}
TABLES['Products_Bugs'] = (
    "CREATE TABLE `Products_Bugs` ("
    "  `id` int(11) NOT NULL AUTO_INCREMENT,"
    "  `brand` varchar(20) NOT NULL,"
    "  `model_name` varchar(30) NOT NULL,"
    "  `price` varchar(30) NOT NULL,"
    "  `wireless_type` varchar(30) NOT NULL,"
    "  `bug_stars` varchar(4) NOT NULL,"
    "  `bug_title` varchar(30) NOT NULL,"
    "  `bug_content` TEXT NOT NULL,"
    "  `bug_author` varchar(20) NOT NULL,"
    "  `available_date` date NOT NULL,"
    "  `bug_date` date NOT NULL,"
    "  `query_date` date NOT NULL,"
    "  PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB")




cnx = mysql.connector.connect(user='root',password='12345678')
cursor = cnx.cursor()


def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

try:
    cnx.database = DB_NAME
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        cnx.database = DB_NAME
    else:
        print(err)
        exit(1)


for name, ddl in TABLES.items():
    try:
        print("Creating table {}: ".format(name), end='')
        cursor.execute(ddl)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")

cursor.close()
cnx.close()







