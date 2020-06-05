#7-4
pizzas = ''
while pizzas != 'quit':
    pizzas = input("请输入披萨配料：")
    if pizzas != 'quit':
        print("We will add this " + pizzas.title() + " in your pizzas!")

#7-5
age = ("请问你的年龄多大？")

while True:
    inputage  = input(age)
    if '退出' in inputage:
        print("程序结束")
        break
    elif int(inputage) < 3:
        print("您的票价免费！")
    elif 3 <= int(inputage) <= 12:
        print("您的票价10美元")
    elif int(inputage) > 12:
        print("您的票价15美元")
