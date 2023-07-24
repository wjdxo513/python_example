# demo_mysql01.py
import mysql.connector 
conn = mysql.connector.connect(user='jonathan', password='1234', host='127.0.0.1')
print(conn)
conn.close()
