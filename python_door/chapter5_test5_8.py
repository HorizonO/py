users = ['admin','edison','sanyu','kris','wu']
user = input("请输入用户名：")
if user == 'admin':
    print('Hello ' + user + ',would you like to see a status report?')
if user == '':
    print('We need to find some users!')
else:
    print(user + ',thank you for logging again!')