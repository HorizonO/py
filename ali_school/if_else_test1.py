x = int(input('请输入一个不超过五位的正整数：'))
if x > 0:
    if len(str(x)) <= 5:
        print("这个正整数是一个",len(str(x)),"数！")
    else:
        print("输入的数长度有误！")
if x < 0:
    print("输入的数不是正整数！")
if x == 0:
    print("Zero")

for i in str(x):
    print(i)
