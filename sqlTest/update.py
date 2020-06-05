import pymysql
db = pymysql.connect("localhost", "root", "root", "library")
cursor = db.cursor()
sql = "select * from book"
cursor.execute(sql)
results = cursor.fetchall()
# 遍历数据库中的每一列
for num in results:
    bookID = num[0]
    bookName = num[1]
    date = num[2]
    price = num[3]
    bookcount = num[4]
    author = num[5]
    #如果bookcount数值小于或者等于5，则修改为10
    sql2 = "update book  set bookcount=10 where bookcount<=5"
    cursor.execute(sql2)
    db.commit()
db.close()