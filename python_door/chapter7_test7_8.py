#7-8熟食店
sandwich_orders = ['火腿三明治','蔬菜三明治','水果三明治']
finished_sandwiches = []
while sandwich_orders:
        sandwich  = sandwich_orders.pop()
        finished_sandwiches.append(sandwich)
        print("我做了你要的 " + sandwich + '。\n')

for finished_sandwiche in finished_sandwiches:
    print(finished_sandwiche)

#7-9五香烟熏牛肉
sandwich_orders = ['火腿三明治','pastrami','蔬菜三明治','pastrami','pastrami','水果三明治']
print('熟食店的五香烟熏牛肉买完了！')
active = True
while active:
    if 'pastrami' in sandwich_orders:
        sandwich_orders.remove('pastrami')
    else:
        active = False
print(sandwich_orders)

#7-10梦想的度假胜地

visitdict = {}
active = True
print("你有没有特别想要去度假的地方？,请完成下面的问卷调查。")
while active:
    name = input("\n请输入您的姓名：")
    visit = input("\n请输入您想去旅游的地方：")
    visitdict[name] = visit
    repeat = input("\n是否还有人要参与问卷调查？(yes/ no)")
    if repeat == 'no':
        active = False
print("\n---结束调查---")
for name,visit in visitdict.items():
    print(name + "想去" + visit + "。")
