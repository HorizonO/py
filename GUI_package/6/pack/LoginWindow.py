from tkinter import messagebox
from  tkinter import *
class Login(object):
    def __init__(self):
        self.root = Tk()# 创建主窗口,用于容纳其它组件
        self.root.resizable(False, False)  # 设置窗口大小不可变
        self.root.title("用户管理系统")# 给主窗口设置标题内容
        curWidth, curHeight = 450, 300  # 设置窗口大小
        scnWidth, scnHeight = self.root.maxsize()  # 获取屏幕大小
        geocnf = '%dx%d+%d+%d' % (curWidth, curHeight,
                (scnWidth - curWidth) / 2, (scnHeight - curHeight) / 2)
        self.root.geometry(geocnf)  #设置窗口大小及窗口在屏幕中的定位（在这里设置为居中）#运行代码时记得添加一个gif图片文件，不然是会出错的
        self.canvas = Canvas(self.root, height=200, width=500)#创建画布  
        self.image_file = PhotoImage(file='D:/timg.gif')#加载图片文件  
        self.image = self.canvas.create_image(0,0, anchor='nw', image=self.image_file)#将图片置于画布上  
        self.canvas.pack(side='top')#放置画布（为上端）  
        #创建一个`label`名为`Account: ` 
        self.label_dl = Label(self.root, text='用户登录')
        self.label_account = Label(self.root, text='用户名: ')
        #创建一个`label`名为`Password: `  
        self.label_password = Label(self.root, text='密   码: ')
        # 创建一个账号输入框,并设置尺寸  
        self.input_account = Entry(self.root, width=30)
        # 创建一个密码输入框,并设置尺寸  
        self.input_password =Entry(self.root, show='*',width=30)
         # 创建一个登录系统的按钮  
        self.login_button = Button(self.root, command = self.backstage_interface, text = "登录", width=10)
        #创建一个注册系统的按钮  
        self.siginUp_button =Button(self.root, command = self.siginUp_interface, text = "注册", width=10)
        # 完成布局
        self.loginuser = 'user.txt'

    def gui_arrang(self):
        self.label_dl.place(x=200, y= 100)
        self.label_account.place(x=80, y= 160)
        self.label_password.place(x=80, y= 195)
        self.input_account.place(x=155, y=160)
        self.input_password.place(x=155, y=195)
        self.login_button.place(x=160, y=235)
        self.siginUp_button.place(x=260, y=235)
        self.input_account.focus()

    # 进入注册界面   
    def siginUp_interface(self):
        self.root.withdraw()
        messagebox.showinfo(title='用户信息管理系统', message='进入首页界面')
        import Register


    #   进行登录信息验证  
    def backstage_interface(self):
        account = self.input_account.get().strip()
        password = self.input_password.get().strip()
        if account == "" or password == "":
            messagebox.showinfo(title='用户信息管理系统', message='账号、密码不能为空!')
        elif account != "" and password != "":
            try:
                f = open(self.loginuser, "r", encoding="utf-8")
                x=False
                for line in f:
                    line = line.strip()
                    line_list = line.split("#")
                    if line_list[0] == account and line_list[1] == password:
                        x=True
                        break
                    elif line_list[0] != account or line_list[1] != password:
                        x=False
                if x==True:
                    self.root.withdraw()  # 隐藏主窗口
                    messagebox.askokcancel(title='用户信息管理系统', message='欢迎进入管理界面')
                    from me import UserManager
                else:
                    messagebox.showinfo(title='用户信息管理系统', message='账号或密码错误，请重新输入!')
                    self.input_account.focus()

            except IOError:
                return False



# 初始化对象  
L = Login()
# 进行布局  
L.gui_arrang()
# 主程序执行  
mainloop()

