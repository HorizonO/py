year=int(input("输入一个年份："))
if year % 100 == 0:
    if year % 400 == 0:
        print('%d年是闰年' %year)
    else:
        print('%d年不是闰年' %year)
else:
    if year%4==0:
        print('%d年是闰年' %year)
    else:
        print('%d年不是闰年' %year)