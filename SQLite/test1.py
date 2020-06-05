import sqlite3
conn = sqlite3.connect(r"f:\userdb.db")
cur = conn.cursor()
cur.execute("create table if not exists book(id primary key text,name text)")
cur.execute("insert into book values(?,?)",("001","大学语文"))
cur.fecthone()  #返回结果集下一行，无数据返回None
cur.fecthall()   #返回结果集剩余行，无数据返回空list
cur.rowcount
conn.commit()   #提交
conn.rollback()
cur.close()     #关闭Cursor对象
conn. close()