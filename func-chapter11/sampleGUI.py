# !/usr/bin/env python
# coding=utf-8

"""first GUI program with Tkinter"""

from functools import partial as ma
import Tkinter

root = Tkinter.Tk()
MyButton = ma(Tkinter.Button, root, fg='white', bg='blue')

b1 = MyButton(text='确定')
b2 = MyButton(text='取消')
qb = MyButton(text='退出', bg='red', command=root.quit)

b1.pack()
b2.pack()
qb.pack(fill=Tkinter.X, expand=True)

root.title('第一个 GUI')
root.mainloop()
