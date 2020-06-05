from tkinter import *
# 创建窗口
root = Tk()
# 创建并添加Canvas
cv = Canvas(root, background='skyblue')
cv.pack(fill=BOTH, expand=YES)
cv.create_rectangle(30, 30, 200, 200,
    outline='blue', # 边框颜色
    stipple = 'question', # 填充的位图
    fill="red", # 填充颜色
    width=5 # 边框宽度
    )
cv.create_oval(240, 30, 330, 200,
    outline='red', # 边框颜色
    fill='pink', # 填充颜色
    width=4 # 边框宽度
    )
root.mainloop()