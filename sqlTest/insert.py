import pymysql

# 打开数据库连接
db = pymysql.connect("localhost", "root", "root", "library")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

sql="insert into book(bookID,bookName,date,price,bookcount,author) " \
    "values ('5','计算机操作原理','2016-3-6',48,4,'林原理')"
# 使用 execute()  方法执行 SQL 查询
try:
   # 执行sql语句
   cursor.execute(sql)
   # 提交到数据库执行
   db.commit()
except:
   # 如果发生错误则回滚
   db.rollback()
# 关闭数据库连接
db.close()