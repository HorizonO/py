alien_color = 'green'
if alien_color == 'green':
    print("You have 5 points!")
elif alien_color == 'yellow':
    print("10 points!")
else:
    print("15 points!")

#5-6
age = int(input("请输入年龄："))
if age < 2:
    print('He is a baby.')
elif age < 4:
    print("He is learing.")
elif age<13:
    print('children.')
elif age<20:
    print('tennager.')
elif age<65:
    print('adult')
else:
    print('old')


#5-7
favorite_fruit = ['apple','orange','banana']
if 'apple' in favorite_fruit:
    print('yeap')
if 'orange' in favorite_fruit:
    print('yeep')
if 'banana' in favorite_fruit:
    print('yes')
if 'mi' not in favorite_fruit:
    print('no')
print('You really like bananas!')