import pymysql.cursors
 
conn = pymysql.connect(host='localhost',
        user='root',
        password='1234',
        db='test',
        charset='utf8mb4')
 
try:
    with conn.cursor() as cursor:
        sql = 'INSERT INTO users (email, password) VALUES (%s, %s)'
        cursor.execute(sql, ('test@test.com', 'my-passwd'))
    conn.commit()
    print(cursor.lastrowid)
    # 1 (last insert id)
finally:
    conn.close()