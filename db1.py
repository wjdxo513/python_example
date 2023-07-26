# db1.py

import sqlite3

#연결 객체 생성 (일단은 메모리에서 연습)
con = sqlite3.connect(":memory:")

#커서 객체
cur = con.cursor()

#테이블 구조 생성
cur.execute("create table if not exists PhoneBook " + 
            " (id integer primary key autoincrement, " +
            " name text, phoneNum text);")
            
#1건 입력
cur.execute("insert into PhoneBook (name, phoneNum) values " + "('홍길동', '010-111');")

# 입력 파라메터 처리
name = "전우치"
phoneNumber = "010-222"
cur.execute("insert into PhoneBook (name, phoneNum) values " + " (?, ?);", (name, phoneNumber))


#다중의 행을 입력
datalist = (("이순신","010-333"), ("박문수","010-123"))
cur.executemany("insert into PhoneBook (name, phoneNum) values " + "(?, ?);", datalist)


#검색 구문
cur.execute("select * from PhoneBook;")
print("---fetchone()---")
print(cur.fetchone())
print("---fetchmany(2)---")
print(cur.fetchmany(2))
print("---fetchall()---")
cur.execute()
print(cur.fetchall())


#for row in cur:
#    print(row)
