#!/usr/bin/python
# -*- coding: UTF-8 -*-

import tkinter as tk
window = tk.Tk()
tk.Label(window,text="GUI,")
window.title("My window")
window.geometry("500x200")
# window.mainloop()
#获取屏幕分辨率
window.winfo_screenwidth()
window.winfo_screenheight()
#获取窗口宽度和高度
w=window.winfo_reqwidth()
h=window.winfo_reqheight()

print(w,h)
