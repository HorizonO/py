from tkinter import *
from tkinter import messagebox
class Register(object):

    def __init__(self):
        self.reg = Toplevel()# 创建主窗口,用于容纳其它组件
        self.reg.resizable(False, False)  # 设置窗口大小不可变
        self.reg.title("用户注册系统")# 给主窗口设置标题内容
        curWidth, curHeight = 450, 300  # 设置窗口大小
        scnWidth, scnHeight = self.reg.maxsize()  # 获取屏幕大小
        geocnf = '%dx%d+%d+%d' % (curWidth, curHeight, (scnWidth - curWidth) / 2, (scnHeight - curHeight) / 2)
        self.reg.geometry(geocnf)  #设置窗口大小及窗口在屏幕中的定位（在这里设置为居中）#运行代码时记得添加一个gif图片文件，不然是会出错的
        self.canvas = Canvas(self.reg, height=300, width=500)  # 创建画布  
        self.image_file = PhotoImage(file='F:/timg.gif')  # 加载图片文件  
        self.image = self.canvas.create_image(0, 0, anchor='nw', image=self.image_file)  # 将图片置于画布上  
        self.canvas.pack(side='top')  # 放置画布（为上端） 
        #创建一个`label`名为`Account: ` 
        self.label_dl = Label(self.reg, text='用户注册', font=("黑体", 20),fg="red" ) # 字体颜色)
        self.label_account = Label(self.reg, text='用户名: ')
        #创建一个`label`名为`Password: `  
        self.label_password1 = Label(self.reg, text='密   码: ')
        # 创建一个账号输入框,并设置尺寸  
        self.account = Entry(self.reg, width=30)
        # 创建一个密码输入框,并设置尺寸  
        self.password1 =Entry(self.reg, show='*',width=30)
        #创建一个`label`名为`Password: `  
        self.label_password2 = Label(self.reg, text='确认密码: ')
        # 创建一个密码输入框,并设置尺寸  
        self.password2 =Entry(self.reg, show='*',width=30)
         # 创建一个确认按钮  
        self.ok_button = Button(self.reg, command = self.isok, text = "确定", width=10)
        #创建一个重置按钮  
        self.siginUp_button =Button(self.reg, command = self.isclear, text = "重置", width=10)
        #创建一个返回登录按钮  
        #self.login_button =Button(self.reg, command = self.relogin, text = "返回登录", width=10)
        # 完成布局  
        self.loginuser = 'user.txt'
    def isok(self):
        user = self.account.get().strip()
        p1 = self.password1.get().strip()
        p2 = self.password2.get().strip()
        if user=="" or p1=="" or p2=="":
            messagebox.showerror(title='用户注册', message='用户名、密码都不能为空，请输入!')
        elif user!="" and p1!="" and p2!="":
            if p1==p2:
                str = user + '#' + p1
                try:
                    f = open(self.loginuser, "a+", encoding="utf-8")
                    f.write("\n" + str)
                    messagebox.showinfo(title='用户注册', message='注册成功!')
                except IOError:
                    return False
            else:
                messagebox.showerror(title='用户注册', message='密码不一致，请重新输入!')


    def isclear(self):
        self.account.set('')
        self.password1.set('')
        self.password2.set('')



    def gui_arrang(self):
        self.label_dl.place(x=180, y= 90)
        self.label_account.place(x=80, y= 160)
        self.label_password1.place(x=80, y= 195)
        self.label_password2.place(x=80, y= 235)
        self.account.place(x=155, y=160)
        self.password1.place(x=155, y=195)
        self.password2.place(x=155, y=235)
        self.ok_button.place(x=140, y=265)
        self.siginUp_button.place(x=230, y=265)


r = Register()
# 进行布局  
r.gui_arrang()
# 主程序执行  
mainloop()

