# 导入模块
from tkinter import *
from tkinter.messagebox import *

class Usermanager(object):
# 创建顶层（根）窗口

    def __init__(self):
        self.user = Toplevel()
        self.systitle='用户注册信息管理系统'
        self.user.resizable(False, False) #设置窗口大小不可变
        self.user.title(self.systitle)
        self.curWidth, self.curHeight = 500, 300  #设置窗口大小
        self.scnWidth, self.scnHeight = self.user.maxsize()   #获取屏幕大小
        self.geocnf = '%dx%d+%d+%d' % (self.curWidth, self.curHeight,(self.scnWidth - self.curWidth) / 2, (self.scnHeight - self.curHeight) / 2)
        self.user.geometry(self.geocnf)  #设置窗口大小及窗口在屏幕中的定位（在这里设置为居中）
        # 功能界面
        self.mainframe = LabelFrame()
        self.mainframe.pack()

        # 数据库名
        self.dbfile = 'userdb.dat'
        # 异常日志文件名
        self.logfile = 'user_management_error.log'


# 获取数据库连接
    def getconn(self):
        try:
            import sqlite3
            conn = sqlite3.connect(self.dbfile)
            return conn
        except Exception as ex:
            print('数据库访问出错：', ex)
            raise ex  # 向外传递异常，以便统一写入日志
    # 显示全部用户
    def showall(self):
        self.mainframe.destroy()
        conn =self.getconn()
        cur = conn.execute('select * from user')
        users = cur.fetchall()
        conn.close()
        if len(users) == 0:
            showwarning(self.systitle, '当前没有注册用户！')
        else:
            self.mainframe = LabelFrame(self.user,text='全部注册用户')
            self.mainframe.pack(anchor=CENTER, padx=25, pady=25, ipadx=25, ipady=25)
            self.mainframe.columnconfigure(1, minsize=80)
            self.mainframe.columnconfigure(2, minsize=200)
            self.mainframe.columnconfigure(3, minsize=200)
            Label(self.mainframe, text='序号', font=('宋体', 12, 'bold'),
                  bd=1, relief=SOLID).grid(row=1, column=1, sticky=N + E + S + W)
            Label(self.mainframe, text='用户名', font=('宋体', 12, 'bold'),
                  bd=1, relief=SOLID).grid(row=1, column=2, sticky=N + E + S + W)
            Label(self.mainframe, text='密码', font=('宋体', 12, 'bold'),
                  bd=1, relief=SOLID).grid(row=1, column=3, sticky=N + E + S + W)
            rn = 2  # 行号
            for user in users:
                cn = 1  # 列号
                Label(self.mainframe, text=str(rn - 1), font=('宋体', 12), bd=1,
                      relief=SOLID).grid(row=rn, column=cn, sticky=N + E + S + W)
                for field in user:
                    cn = cn + 1
                    Label(self.mainframe, text=str(field), font=('宋体', 12), bd=1,
                          relief=SOLID).grid(row=rn, column=cn, sticky=N + E + S + W)
                rn = rn + 1


    # 重置数据库
    def resetdb(self):
        self.mainframe.destroy()

        msg = '将删除全部注册用户！\n请你确认是否要继续？'
        if askokcancel(self.systitle, msg):
            import os
            if os.path.exists(self.dbfile):
                os.remove(self.dbfile)
                showinfo(self.systitle, '系统重置数据库！')
            else:
                showinfo(self.systitle, '系统创建数据库！')
            conn = self.getconn()
            conn.execute('create table user(username text primary key, password text)')
            conn.close()
        # 查找用户名是否存在
    def find(self,username):
        conn = self.getconn()
        cur = conn.execute('select * from user where username = ? ', (username,))
        users = cur.fetchall()
        conn.close()
        if len(users) > 0:
            return True
        else:
            return False
    # 添加用户
    def adduser(self):
        self.mainframe.destroy()
        self.mainframe = LabelFrame(self.user,text='添加新用户')
        self.mainframe.pack(anchor=CENTER, pady=20, ipadx=5, ipady=5)
        self.mainframe.pack()
        def totxtpassword(event):
            txtpassword.focus()

        def tobtnsave(event):
            btnsave.focus()

        frmtop = Frame(self.mainframe)
        frmtop.pack()
        Label(frmtop, text='用户名：', anchor=E).grid(row=1, column=1)
        username = StringVar()
        txtusername = Entry(frmtop, textvariable=username)
        txtusername.grid(row=1, column=2)
        txtusername.bind('<Return>', totxtpassword)
        txtusername.focus()
        Label(frmtop, text='密   码：', anchor=E).grid(row=2, column=1)
        password = StringVar()
        txtpassword = Entry(frmtop, textvariable=password, show='*')
        txtpassword.grid(row=2, column=2)
        txtpassword.bind('<Return>', tobtnsave)

        frmbottom = Frame(self.mainframe)
        frmbottom.pack(pady=5)
        btnsave = Button(frmbottom, text='保存',width=8)
        #btnsave.config(width=8, activeforeground='red')
        btnsave.grid(row=1, column=1)
        btnclear = Button(frmbottom, text='重置', width=8)
        #btnclear.config(width=8, activeforeground='red')
        btnclear.grid(row=1, column=2)

        def save():
            username = txtusername.get()
            password = txtpassword.get()
            if username == '':
                showerror(self.systitle, '用户名不能为空！')
            else:
                if self.find(username):
                    showerror(self.systitle, '用户名已存在，重新输入用户名！')
                    txtusername.focus()
                    txtusername.select_range(0, END)
                else:
                    if password == '':
                        showerror(self.systitle, '密码不能为空！')
                        txtpassword.focus()
                    else:
                        conn = self.getconn()
                        conn.execute('insert into user values(?, ?)', (username, password))
                        conn.commit()
                        conn.close()
                        showinfo(self.systitle, '成功添加用户[' + username + ']！')
        def clear():
            username.set('')
            password.set('')
            txtusername.focus()

        btnclear.config(command=clear)
        btnsave.config(command=save)
    # 查找、修改或删除
    def check_update(self):
        #global mainframe
        self.mainframe.destroy()

        self.mainframe = LabelFrame(self.user,text='查找、修改或删除用户', width=400, height=300)
        self.mainframe.pack(anchor=CENTER, pady=20, ipadx=5, ipady=5)

        findframe = LabelFrame(self.mainframe, text='查找用户')
        findframe.pack(anchor=CENTER, padx=10, ipadx=5, ipady=5, fill=X)
        Label(findframe, text='输入待查用户名：', anchor=E).grid(row=1, column=1)
        username = StringVar()
        txtusername = Entry(findframe, textvariable=username)
        txtusername.grid(row=1, column=2)
        txtusername.focus()
        btnfind = Button(findframe, text='查找')
        btnfind.grid(row=1, column=3)

        deleteframe = LabelFrame(self.mainframe, text='删除用户')
        deleteframe.pack(anchor=CENTER, padx=10, ipadx=5, ipady=5, fill=X)
        btndelete = Button(deleteframe, text='删除用户', state=DISABLED)
        btndelete.pack(fill=X, padx=10)

        editframe = LabelFrame(self.mainframe, text='修改用户')
        editframe.pack(anchor=CENTER, padx=10, ipadx=5, ipady=5, fill=X)
        Label(editframe, text='新用户名：').grid(row=1, column=1)
        newusername = StringVar()
        txtnewusername = Entry(editframe, textvariable=newusername)
        txtnewusername.grid(row=1, column=2)
        Label(editframe, text='新 密 码：').grid(row=2, column=1)
        newpassword = StringVar()
        txtnewpassword = Entry(editframe, textvariable=newpassword, show='*')
        txtnewpassword.grid(row=2, column=2)
        btnupdate = Button(editframe, text='更新用户信息', state=DISABLED)
        btnupdate.grid(row=1, column=3, rowspan=2, sticky=N + S)


        def finduser():
            username = txtusername.get()
            if not self.find(username):
                showinfo(self.systitle, '[%s]还未注册！' % username)
            else:
                btndelete.config(state=NORMAL)
            btnupdate.config(state=NORMAL)


        def deleteuser():
            username = txtusername.get();
            if askyesno(self.systitle, '要删除用户[%s]吗？' % username):
                conn = self.getconn()
                conn.execute('delete from user where username = ?', (username,))
                conn.commit()
                conn.close()
                showinfo(self.systitle, '成功删除用户[%s]！' % username)
                txtusername.delete(0, END)
                btndelete.config(state=DISABLED)
                btnupdate.config(state=DISABLED)


        def updateuser():
            username = txtusername.get()
            newusername = txtnewusername.get()
            if newusername == '':
                showerror(self.systitle, '新用户名不能为空！')
                txtnewusername.focus();
            else:
                if self.find(newusername):
                    showerror(self.systitle, '用户名[%s]已经注过册！' % newusername)
                    txtnewusername.focus()
                else:
                    newpassword = txtnewpassword.get();
                    if newpassword == '':
                        showerror(self.systitle, '密码不能为空！')
                    else:
                        conn = self.getconn()
                        conn.execute('update user set username = ?, password = ? where username = ?',
                                     (newusername, newpassword, username))
                        conn.commit()
                        conn.close()
                        showinfo(self.systitle, '用户数据更新成功！')


        btnfind.config(command=finduser)
        btndelete.config(command=deleteuser)
        btnupdate.config(command=updateuser)

    # 退出系统
    def exit(self):
        if askokcancel(self.systitle, '你要退出系统吗？'):
            self.user.quit()
            self.user.destroy()

    def menubar(self):
        # 创建菜单系统
        menubar = Menu(self.user)#为root窗口创建菜单栏功能
        self.user.config(menu=menubar)  #等同root['menu']=menubar
        m = Menu(menubar, tearoff=0) #创建一个名为m的菜单选项
        menubar.add_cascade(label='系统操作', menu=m)#名为m的菜单选项设置标签
        m.add_command(label='创建/重置用户数据库', command=self.resetdb) #为m菜单项添加菜单选项,并设置操作命令
        m.add_separator()   #设置分隔线
        m.add_command(label='添加新用户', command=self.adduser)
        m.add_command(label='显示全部注册用户', command=self.showall)
        m.add_command(label='查找/修改/删除用户', command=self.check_update)
        m = Menu(menubar, tearoff=0)
        menubar.add_cascade(label='退出系统', menu=m)
        m.add_command(label='退出系统', command=exit)



L=Usermanager()
L.menubar()
mainloop()
