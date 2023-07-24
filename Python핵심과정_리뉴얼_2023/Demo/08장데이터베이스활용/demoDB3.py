# demoDB3.py 
import sqlite3

con = sqlite3.connect("c:\\work\\sample.db")
#SQL구문을 실행할 커서 객체 리턴
cur = con.cursor()

#결과를 확인
cur.execute("select * from PhoneBook;")
for row in cur:
    print(row)


