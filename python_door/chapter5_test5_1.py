#coding=utf-8
car = 'subaru'
print("Is car == 'subaru'?I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'?Ipredict False.")
print(car == 'audi')

age = int(input("输入年龄："))
if age >= 18:
    print("You are old enough to vote!")
else:
    print("You can not vote!")

alien_color = str(input('输入外星人颜色：'))
if 'green' is alien_color:
    print("You have 5 point!")
if 'yellow' is alien_color:
    print("You have 10 point!")
if 'red' is alien_color:
    print('You have 15 point!')