import wx

# import the newly created GUI file
import demo


class CalcFrame(demo.MyFrame1):
    def __init__(self, parent):
        demo.MyFrame1.__init__(self, parent)

    def findsquare(self, event):
        num = int(self.m_textCtrl1.GetValue())
        self.m_textCtrl2.SetValue(str(num * num))


app = wx.App(False)
frame = CalcFrame(None)
frame.Show(True)
# start the applications
app.MainLoop()

