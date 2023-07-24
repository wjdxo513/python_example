import pymysql.cursors
 
conn = pymysql.connect(host='localhost',
        user='root',
        password='1234',
        db='test',
        charset='utf8mb4')
 
try:
    with conn.cursor() as cursor:
        sql = 'SELECT * FROM users WHERE email = %s'
        cursor.execute(sql, ('test@test.com',))
        result = cursor.fetchone()
        print(result)
        # (1, 'test@test.com', 'my-passwd')
except:
    pass


#수정
try:
    with conn.cursor() as cursor:
        sql = 'UPDATE users SET email = %s WHERE email = %s'
        cursor.execute(sql, ('my@test.com', 'test@test.com'))
    conn.commit()
    print(cursor.rowcount) # 1 (affected rows)
except:
    pass
    
#삭제
try:
    with conn.cursor() as cursor:
        sql = 'DELETE FROM users WHERE email = %s'
        cursor.execute(sql, ('my@test.com',))
    conn.commit()
    print(cursor.rowcount) # 1 (affected rows)
finally:
    conn.close()