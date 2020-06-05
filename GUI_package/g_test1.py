from tkinter import *

root = Tk()
MainLabel = Label(root,text="TKinter GUI,我很丑，但我易学",font="Times 16 bold",bg='skyblue',fg="purple")
MainLabel.pack()  #显示Label标签
root.title("窗口标题")
root.resizable(False,False)
root.update()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
w_width = root.winfo_reqwidth()
w_height = root.winfo_reqheight()
tmpcnf = '%dx%d+%d+%d'%(w_width,w_height,(screen_width-w_width)/2,(screen_height-w_height)/2)
root.geometry(tmpcnf)

root.mainloop()