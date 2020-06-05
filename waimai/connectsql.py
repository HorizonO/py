import pymysql
conn = pymysql.connect("localhost",'root','root','student',charset='utf8')
cursor = conn.cursor()
cursor.execute("select * from student")
data = cursor.fetchone()
print(data)
conn.close()