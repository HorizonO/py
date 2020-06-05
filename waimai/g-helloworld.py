import wx
app = wx.App()
window = wx.Frame(None,title='login',size=(400,300))
panel = wx.Panel(window)
label = wx.StaticText(panel,label="Hello,World!",pos = (100,100))
window.Show(True)
app.MainLoop()