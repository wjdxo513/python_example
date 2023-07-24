# Demo_tableCreate.py
import pymysql.cursors
 
conn = pymysql.connect(host='localhost',
        user='root',
        password='1234',
        db='test',
        charset='utf8mb4')
 
try:
    with conn.cursor() as cursor:
        sql = '''
            CREATE TABLE users (
                id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
                email varchar(255) NOT NULL,
                password varchar(255) NOT NULL
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8
'''
        cursor.execute(sql)
    conn.commit()
finally:
    conn.close()