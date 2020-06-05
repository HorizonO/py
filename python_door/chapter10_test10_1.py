#10-1
# filename = 'learing_python.txt'
# with open(filename) as file_object:
#     lines = file_object.readlines()
# for line in lines:
#     print(line.replace('Python','C').rstrip())

#10-3
# username = str(input("请输入姓名："))
# filename = 'guest.txt'
# with open(filename,'w') as file_object:
#     file_object.write(username)

#10-4
# filename = 'guest_book.txt'
# with open(filename,'a') as file_object:
#     print('按‘q’推出')
#     while True:
#         name = input('请输入你的名字：')
#         if name == 'q':
#             break
#         file_object.write(name + '\n')
#         print("Hello " + name)

#10-5
filename = 'guest_book.txt'
with open(filename,'a') as file_object:
    print('按null退出')
    while True:
        result = str(input("你为什么喜欢编程？"))
        if result == 'null':
            break
        file_object.write(result + '\n')





