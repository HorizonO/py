import csv
with open('Exam2.2.csv',encoding='utf-8')as f:
   reader=[x for x in csv.DictReader(f)]
for row in reader:
       username=row['username']
       content=row['content']
       reply_time=row['reply_time']
       print('用户名:{},回复内容:{}'.format(username,content))