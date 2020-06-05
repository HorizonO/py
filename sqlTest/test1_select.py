import pymysql
from datetime import datetime
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
    #获取日期中的年份信息
    time = datetime.strptime(date,'%Y-%m-%d')
    #把年份赋值给ty
    ty = time.year

    #增加条件，如果ty是2018，输出信息
    if ty == 2018:
        print("bookId: " + bookID + ", bookName:" + bookName + ", date:" + date +
          ", price:" + price + ", bookcount:" + bookcount + ", author:" + author)

db.close()
