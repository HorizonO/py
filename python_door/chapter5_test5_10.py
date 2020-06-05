current_users = ['a','b','c','d','e']
new_users = ['a','c','f','g','s']
for new_user in new_users:
    if new_user in current_users:
        print(new_user + "用户名已用！")
    else:
        print(new_user + "未被使用！")