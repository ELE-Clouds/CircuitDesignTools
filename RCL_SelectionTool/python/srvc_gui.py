#!/usr/bin/
# -*- coding: utf-8 -*-
'''
*************************************************
  文件名：srvc_GUI
  Copyright (C), 2016, ELE-Clouds.All rights reserved.
  作者：ELE-Clouds
  日期：2016年12月15日
  版本：V0.01
  描述:
        本程序主要用于srvc_mod模块的界面显示和参数输入。
        本程序主要用于调用并显示 srvc_mod 模块的相关函数
        与结果。            
                  
  主要函数列表:   //每条记录应包括函数名及功能简要说明
    1. is_number(s)        判断字符串是否为数字
    2. clickMe()           按扭的动作函数，提交输入框内容，并显示返回结果。

  修改历史记录：: 
    1.修改日期:
       修改人:
       修改内容:
    2. ....
*************************************************
'''

import Tkinter as tk
import ttk as ttk
import srvc_mod
#import tkFont
import tkMessageBox

win = tk.Tk()
win.title("标准阻值计算器   V1.0")    #添加标题
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


'''
*************************************************
  函数名称：is_number       
  描述:                           # 函数功能、性能等的描述
      判断参数值是否为数字

  调用函数：             // 被本函数调用的函数清单
      unicodedata.numeric(s)

  被调用函数：          // 调用本函数的函数清单
      clickMe()

  访问表:               // 被访问的表（此项仅对于牵扯到数据库操作的程序）
  修改表:               // 被修改的表（此项仅对于牵扯到数据库操作的程序）
  输入参数:               // 输入参数说明，包括每个参数的作
      s        用于接收输入框内的值

  输出参数:               // 对输出参数的说明。

  返回值:                  // 函数返回值的说明
      True/False          如果判断参数值是数字，则返回True，否则返回False

  其它说明:               // 其它说明
*************************************************
'''
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



'''
*************************************************
  函数名称：clickMe        
  描述:                           # 函数功能、性能等的描述
      button 被点击之后会被执行

  调用函数：             // 被本函数调用的函数清单
      srvc_mod.val_Srv(val_resistance,num_id,str_formula='2')
      is_number(s)

  被调用函数：          // 调用本函数的函数清单
      
  访问表:               // 被访问的表（此项仅对于牵扯到数据库操作的程序）
  修改表:               // 被修改的表（此项仅对于牵扯到数据库操作的程序）
  输入参数:               // 输入参数说明，包括每个参数的作
      无                  // 用、取值说明及参数间关系。
  输出参数:               // 对输出参数的说明。
      无
  返回值:                  // 函数返回值的说明
      无  
  其它说明:               // 其它说明
*************************************************
'''
def clickMe():
    #提交前内容检查
    if not(name.get()):
    	tkMessageBox.showwarning("警告", "输入框内不能为空！")
    	return
    if not(is_number(name.get())):
    	tkMessageBox.showwarning("警告", "输入框内只能输入数值！")
    	return

    lis_value=[]
    lis_value=srvc_mod.val_Srv(name.get(),numberChosen.current())   #srvc_mod.val_Srv函数隐含一个默认参数，用于选择计算数值所用的公式，默认选择最后一个公式。
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
numberChosen['values']=(' 20%  (M)    E6  ',' 10%  (K)    E12 ','  5%  (J)    E24 ','  2%  (G)    E48 ','  1%  (F)    E96 ','0.5%  (D)    E192')
numberChosen['state']='readonly'
numberChosen.grid(column=1,row=2,pady=5)
numberChosen.current(2)


win.mainloop()
