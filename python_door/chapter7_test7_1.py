#7-1
car = input("请输入你想要的汽车：")
print("Let me see if I can find you a " + car + "。")
#7-2
people = int(input("请问有多少人就餐？\n"))
if people <= 8:
    print("有空桌。")
else:
    print("没有空桌！")

#7-3
num = int(input("请输入一个数："))
if num%10 == 0:
    print("这个数字是十的整倍数。")
else:
    print("这个数字不是十的整倍数。")