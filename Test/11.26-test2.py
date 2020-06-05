four = input("请输入一个四位整数：")
sum = 0
def lucky():
    print("这是一个幸运数",four)
def unlucky():
    print("这不是一个幸运数",four)
for i in four:
    sum += int(i)
print("各位数相加和为：",sum)
if sum == 8:
    lucky()
else:
    unlucky()