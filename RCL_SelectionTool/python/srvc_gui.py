'''
srvc_mod.py的界面程序
'''

#!/usr/bin/
# -*- coding: utf-8 -*-


import Tkinter as tk
import ttk as ttk
import srvc_mod
#import tkFont
import tkMessageBox

win = tk.Tk()
win.title("标准阻值计算器")    #添加标题
win.resizable(0, 0)
# 设置窗体大小，使用的是字母x
#win.geometry('500x300')
#fon_title=tkFont.Font(family='黑体',size=24,weight='bold')

fr_view=tk.Frame(win,width=300,height=100,bg='black').grid(column=0,row=5,columnspan=5,rowspan=2,padx=10,pady=10)

tk.Label(win,text='标准阻值计算',font=('微软雅黑', 20)).grid(column=0,row=0,pady=20,columnspan=3)
tk.Label(win,text='电阻值：').grid(column=0,row=1)
tk.Label(win,text='精度值：').grid(column=0,row=2)
tk.Label(win,text='ohm').grid(column=2,row=1)
tk.Label(win,text='<<<',bg='black',fg='white').grid(column=0,row=5)
tk.Label(win,text='推荐值',bg='black',fg='white').grid(column=1,row=5)
#ttk.Label(win,text='偏大值').grid(column=2,row=4)
tk.Label(win,text='<<<',bg='black',fg='white').grid(column=2,row=5)

#偏小值
num_min=tk.StringVar()
num_minView=tk.Label(win,textvariable=num_min,bg='black',fg='white').grid(column=0,row=6)

#推荐值
num_rec=tk.StringVar()
num_recView=tk.Label(win,textvariable=num_rec,bg='black',fg='white').grid(column=1,row=6)

#偏大值
num_max=tk.StringVar()
num_maxView=tk.Label(win,textvariable=num_max,bg='black',fg='white').grid(column=2,row=6)

#判断字符串是否为数字
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
    return False



# button 被点击之后会被执行
def clickMe():
    #name.set(number.get())
    if not(name.get()):
    	tkMessageBox.showwarning("警告", "输入框内不能为空！")
    	return
    if not(is_number(name.get())):
    	tkMessageBox.showwarning("警告", "输入框内只能输入数值！")
    	return

    lis_value=[]
    lis_value=srvc_mod.val_Srv(name.get(),numberChosen.current())
    num_min.set(lis_value[0])
    num_rec.set(lis_value[1])
    num_max.set(lis_value[2])

# 按钮
action = ttk.Button(win,text="开始计算",command=clickMe,width=15)
action.grid(column=1,row=3,pady=10)


# 文本框
name = tk.StringVar()
nameEntered = ttk.Entry(win,width=15,textvariable=name)
nameEntered.grid(column=1,row=1)
nameEntered.focus()


# 创建一个下拉列表
number = tk.StringVar()
numberChosen = ttk.Combobox(win,width=13,textvariable=number)
numberChosen['values']=(' 20%  (M)    E6  ',' 10%  (J)    E12 ','  5%  (K)    E24 ','  2%  (d)    E48 ','  1%  (d)    E96 ','0.5%  (D)    E192')
numberChosen['state']='readonly'
numberChosen.grid(column=1,row=2,pady=5)
numberChosen.current(2)


win.mainloop()
