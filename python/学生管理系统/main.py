from tkinter import *

win=Tk()

#设置界面大小
win.geometry('600x400')
win.title("学生管理系统")

T1=Label(win,text="学生管理系统",font="30")
T1.pack(pady=80)

B1=Button(win,width=10,text="登陆")
B1.pack(side=LEFT,padx=150)

B2=Button(win,width=10,text="注册")
B2.pack(side=LEFT)

win.mainloop()