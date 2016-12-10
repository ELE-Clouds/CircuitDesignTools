#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
# 以下为要用到的math函数
# math.log(值,底数)  eg. 求2自乘了几次等于8， math.log(8,2)
# math.sqrt(值)  开平方  eg. math.sqrt(16) 结果是：4.0
# x**(1/n)：表示求 开x的n方根。  eg.  8**(1.0/3)  求8的3次方根，结果为2.  注意：括号内必须有一个数为浮点数，即整数后加".0"。 
# 其它函数：
# round(值,小数位数)   对值保留一定的小数位数，并进行四舍五入。
'''

import math

dic_EIA={'E6':6,'E12':12,'E24':24,'E48':48,'E96':96,'E192':192}
Ni=['E6','E12','E24','E48','E96','E192']
lis_eia = [6,12,24,48,96,192]

lis_JD = [0.2,0.1,0.05,0.02,0.01,0.005]   #精度值，即误差值，20%的值为20/100=0.2
lis_GBDoc = [2,2,2,3,3,3]     #公比小数位，即“i/N”的小数位数，基值小数位为公比小数位减1，若不按此保留，结果将会出错。
dec = 0         #整数位个数
lis_Val = []    #值的列表


'''
函数功能：计算当前值左右相邻的标准值
用到的位置：
    position_x：位置，即各值在基本值表中所处的横向位置，对照公式val=(10**n)*(10**(i/N))中的i；
    position_y：位置，即各值在基本值表中所处的纵向位置，对照公式val=(10**n)*(10**(i/N))中的n；
    eia：系列号，即当前值所在系列的系列号，对照公式val=(10**n)*(10**(i/N))中的N，如E6的系列号即为6；
    decimal：小数位数，即公比需要保留的小数位数

'''
def adjacent_value(position_x,position_y,eia,decimal): 
    li_value = []
    li_adj = [-1,0,1]    #相邻值相对当前值的位置，比其小的用“-1”，比其大的用“+1”，本身为0.
    for num in li_adj:
        li_value.append(round(10**(round((position_y+(int(position_x)+num)/float(eia)),decimal)),decimal-1))
    return li_value

text = raw_input("请输入电阻值：")
id = int(raw_input("请输入标准号："))
#text = '1.0'    #输入的参数值
#EIA = 6          #输入（选择）值
#id = 3            #列表中对应标准的系列的位置号，使用该号，对列表操作起来将更加方便。


#求基值
val_Basic = round(float(text[0:2])/10,lis_GBDoc[id]-1)   #计算基值，基值为整数位保留一位的小数。

#求dot
for te in str(float(text)):
    if te == '.' :
        break    #遇到小数点后跳出循环。
    dec += 1

#求position    
position = math.log(val_Basic,10)*int(lis_eia[id])

lis_Val = adjacent_value(position,dec,lis_eia[id],lis_GBDoc[id])

for val in lis_Val:
    if float(text) < val*(1+lis_JD[id]) and float(text) > val*(1-lis_JD[id]):
        print '符合要求的 E',lis_eia[id],'标准值为：',val
        print lis_JD[id]
        #print lis_
        break

