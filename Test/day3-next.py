
import wx

# app = wx.App()  # 创建一个窗口
# # size 组建本身的大小 size=(width,height)  pos组建在窗体中的位置 pos=(x,y)
# window = wx.Frame(None,title="多多网络订餐管理系统 v1.0",size=(300,200),pos = (500,300)) #窗口
# panel = wx.Panel(window) # 面板
#
# window.Show(True)# 设置窗体显示
# app.MainLoop() # 主窗体运行


app = wx.App()  # 创建一个窗口
# size 组建本身的大小 size=(width,height)  pos组建在窗体中的位置 pos=(x,y)
window = wx.Frame(None,title="多多网络订餐管理系统 v1.0",size=(300,200),pos = (500,300)) #窗口
panel = wx.Panel(window) # 面板
#定义一个文字标签 StaticText
label= wx.StaticText(panel,label="欢迎使用网络订餐管理系统",pos=(10,20))
#定义一个文本框
label = wx.TextCtrl(panel,value="请输入用户名",pos=(10,50),size=(150,25))
window.Show(True)# 设置窗体显示
app.MainLoop() # 主窗体运行
