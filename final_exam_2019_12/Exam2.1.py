import re
with open('Exam2.1.txt','r') as t:
    name = t.read()
user1=re.findall('有效用户(.*?)无效用户',name,re.S)
print('user1的值为:{}'.format(user1))
user2=re.findall('姓名：(.*?)\n',user1[0])
print('真正有效的人名:{}'.format(user2))
