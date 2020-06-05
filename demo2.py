# coding:utf8

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx  # 导入wxpyhton，pyhton自带的GUI库
# import wx.xrc

import pymysql  # 用于操作数据库
import sys
import importlib
importlib.reload(sys)
# sys.setdefaultencoding('utf8')


###########################################################################
## Class MyFrame1
###########################################################################

# 建一个窗口类MyFrame1继承wx.Frame
class MyFrame1(wx.Frame):
    def __init__(self, parent):

    # Wx.Frame (parent, id, title, pos, size, style, name)
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"外卖信息管理系统", pos=wx.DefaultPosition, size=wx.Size(610, 400),style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
        self.Center()  # 居中显示

    # 小构件，如按钮，文本框等被放置在面板窗口。 wx.Panel类通常是被放在一个wxFrame对象中。这个类也继承自wxWindow类。
        self.m_panel1 = wx.Panel(self)
    # 标签，一行或多行的只读文本，Wx.StaticText(parent, id, label, position, size, style)
        self.m_staticText1 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"关于店铺：", (20, 20))
        self.m_button1 = wx.Button(self.m_panel1, wx.ID_ANY, u"店铺信息", (130, 20), wx.DefaultSize,
                               style=wx.BORDER_MASK)
        self.m_button2 = wx.Button(self.m_panel1, wx.ID_ANY, u"店铺上架", (250, 20), wx.DefaultSize,
                               style=wx.BORDER_MASK)
        self.m_button3 = wx.Button(self.m_panel1, wx.ID_ANY, u"店铺下架", (370, 20), wx.DefaultSize,
                               style=wx.BORDER_MASK)

        self.m_staticText2 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"关于派送员：", (20, 90))
        self.m_button4 = wx.Button(self.m_panel1, wx.ID_ANY, u"派送员信息", (130, 90), wx.DefaultSize,
                               style=wx.BORDER_MASK)
        self.m_button5 = wx.Button(self.m_panel1, wx.ID_ANY, u"聘请派送员", (250, 90), wx.DefaultSize,
                               style=wx.BORDER_MASK)
        self.m_button6 = wx.Button(self.m_panel1, wx.ID_ANY, u"解雇派送员", (370, 90), wx.DefaultSize,
                               style=wx.BORDER_MASK)

        self.m_staticText3 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"关于客服人员：", (20, 160))
        self.m_button7 = wx.Button(self.m_panel1, wx.ID_ANY, u"客服人员信息", (130, 160), wx.DefaultSize,
                               style=wx.BORDER_MASK)
        self.m_button8 = wx.Button(self.m_panel1, wx.ID_ANY, u"聘请客服人员", (250, 160), wx.DefaultSize,
                               style=wx.BORDER_MASK)
        self.m_button9 = wx.Button(self.m_panel1, wx.ID_ANY, u"解雇客服人员", (370, 160), wx.DefaultSize,
                               style=wx.BORDER_MASK)

        self.m_staticText4 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"关于订单：", (20, 230))
        self.m_button10 = wx.Button(self.m_panel1, wx.ID_ANY, u"订单信息", (130, 230), wx.DefaultSize,
                                style=wx.BORDER_MASK)
        self.m_button11 = wx.Button(self.m_panel1, wx.ID_ANY, u"学生订餐", (250, 230), wx.DefaultSize,
                                style=wx.BORDER_MASK)
        self.m_button12 = wx.Button(self.m_panel1, wx.ID_ANY, u"取消订单", (370, 230), wx.DefaultSize,
                                style=wx.BORDER_MASK)
        self.m_button13 = wx.Button(self.m_panel1, wx.ID_ANY, u"修改订单", (490, 230), wx.DefaultSize,
                                style=wx.BORDER_MASK)

        self.m_staticText5 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"关于物流：", (20, 300))
        self.m_button14 = wx.Button(self.m_panel1, wx.ID_ANY, u"配送信息", (130, 300), wx.DefaultSize,
                                style=wx.BORDER_MASK)
        self.m_button15 = wx.Button(self.m_panel1, wx.ID_ANY, u"安排配送", (250, 300), wx.DefaultSize,
                                style=wx.BORDER_MASK)
        self.m_button16 = wx.Button(self.m_panel1, wx.ID_ANY, u"取消配送", (370, 300), wx.DefaultSize,
                                style=wx.BORDER_MASK)

    # 按钮绑定对话框的弹出
    # 在创建应用程序时，Bind函数可以将按钮的动作与特定的函数绑定，当按钮上有动作时，这个函数就会启动，从而处理响应的事件。
    # 个Button被单击发生了EVT_BUTTON事件
        self.m_button1.Bind(wx.EVT_BUTTON, MyDialog11(None).OnClick)
        self.m_button2.Bind(wx.EVT_BUTTON, MyDialog12(None).OnClick)
        self.m_button3.Bind(wx.EVT_BUTTON, MyDialog13(None).OnClick)
        self.m_button4.Bind(wx.EVT_BUTTON, MyDialog21(None).OnClick)
        self.m_button5.Bind(wx.EVT_BUTTON, MyDialog22(None).OnClick)
        self.m_button6.Bind(wx.EVT_BUTTON, MyDialog23(None).OnClick)
        self.m_button7.Bind(wx.EVT_BUTTON, MyDialog31(None).OnClick)
        self.m_button8.Bind(wx.EVT_BUTTON, MyDialog32(None).OnClick)
        self.m_button9.Bind(wx.EVT_BUTTON, MyDialog33(None).OnClick)
        self.m_button10.Bind(wx.EVT_BUTTON, MyDialog41(None).OnClick)
        self.m_button11.Bind(wx.EVT_BUTTON, MyDialog42(None).OnClick)
        self.m_button12.Bind(wx.EVT_BUTTON, MyDialog43(None).OnClick)
        self.m_button13.Bind(wx.EVT_BUTTON, MyDialog44(None).OnClick)
        self.m_button14.Bind(wx.EVT_BUTTON, MyDialog51(None).OnClick)
        self.m_button15.Bind(wx.EVT_BUTTON, MyDialog52(None).OnClick)
        self.m_button16.Bind(wx.EVT_BUTTON, MyDialog53(None).OnClick)

        # 设置按钮的背景颜色
        self.m_button1.SetBackgroundColour('#0a74f7')
        self.m_button1.SetForegroundColour('white')
        self.m_button2.SetBackgroundColour('#0a74f7')
        self.m_button2.SetForegroundColour('white')
        self.m_button3.SetBackgroundColour('#0a74f7')
        self.m_button3.SetForegroundColour('white')

        self.m_button4.SetBackgroundColour('#238E23')
        self.m_button4.SetForegroundColour('white')
        self.m_button5.SetBackgroundColour('#238E23')
        self.m_button5.SetForegroundColour('white')
        self.m_button6.SetBackgroundColour('#238E23')
        self.m_button6.SetForegroundColour('white')

        self.m_button7.SetBackgroundColour('#6F4242')
        self.m_button7.SetForegroundColour('white')
        self.m_button8.SetBackgroundColour('#6F4242')
        self.m_button8.SetForegroundColour('white')
        self.m_button9.SetBackgroundColour('#6F4242')
        self.m_button9.SetForegroundColour('white')

        self.m_button10.SetBackgroundColour('#8E6B23')
        self.m_button10.SetForegroundColour('white')
        self.m_button11.SetBackgroundColour('#8E6B23')
        self.m_button11.SetForegroundColour('white')
        self.m_button12.SetBackgroundColour('#8E6B23')
        self.m_button12.SetForegroundColour('white')
        self.m_button13.SetBackgroundColour('#8E6B23')
        self.m_button13.SetForegroundColour('white')

        self.m_button14.SetBackgroundColour('#545454')
        self.m_button14.SetForegroundColour('white')
        self.m_button15.SetBackgroundColour('#545454')
        self.m_button15.SetForegroundColour('white')
        self.m_button16.SetBackgroundColour('#545454')
        self.m_button16.SetForegroundColour('white')

        self.m_panel1.SetBackgroundColour('white')  # 设置面板的背景颜色