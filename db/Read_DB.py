import datetime
import mysql.connector

cnx = mysql.connector.connect(user='root',password='12345678', database='Amazon_Parse_Bugs')
cursor = cnx.cursor()

query = ("SELECT bug_title, bug_content FROM Products_Bugs "
         "WHERE id = 1")


cursor.execute(query)

for i in cursor:
    print (i)

cursor.close()
cnx.close()