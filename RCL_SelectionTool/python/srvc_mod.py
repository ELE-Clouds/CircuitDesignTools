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

#dic_EIA={'E6':6,'E12':12,'E24':24,'E48':48,'E96':96,'E192':192}
#Ni=['E6','E12','E24','E48','E96','E192']


'''
函数功能：计算当前值左右相邻的标准值
用到的位置：
    num_i：位置，即各值在基本值表中所处的横向位置，对照公式val=(10**n)*(10**(i/N))中的i；
    num_n：位置，即各值在基本值表中所处的纵向位置，对照公式val=(10**n)*(10**(i/N))中的n；
    num_id：系列号列表中对应值得索引值，即当前值所在系列的系列号，对照公式val=(10**n)*(10**(i/N))中的N，如E6的系列号即为6；
    

'''
def adjacent_value(num_n,num_i,num_id): 
    lis_eia = [6,12,24,48,96,192]
    lis_gbDec = [2,2,2,3,3,3]    #标准值保留的小数位数
    li_value = []
    li_adj = [-1,0,1]    #相邻值相对当前值的位置，比其小的用“-1”，比其大的用“+1”，本身为0.
    for num in li_adj:
        #li_value.append(round(10**(num_n+round((num_i+num)/float(lis_eia[num_id]),lis_gbDec[num_id])),lis_gbDec[num_id]-1))
        li_value.append(round(10**(round((num_i+num)/float(lis_eia[num_id]),lis_gbDec[num_id])),lis_gbDec[num_id]-1))
    return li_value



#求标准值函数
def val_Srv(val_resistance,num_id):
    lis_eia = [6,12,24,48,96,192]  #EIA标准号对应的值
    lis_jd = [0.2,0.1,0.05,0.02,0.01,0.005]   #精度值，即误差值，20%的值为20/100=0.2
    lis_gbDec = [2,2,2,3,3,3]     #公比小数位，即“i/N”的小数位数，基值小数位为公比小数位减1，若不按此保留，结果将会出错。
    num_dec = 0         #整数位个数,即i
    list_value=[]
    val_resistance = float(val_resistance)
    num_id=int(num_id)
    for te in str(float(val_resistance)):
        if te == '.' :
            break    #遇到小数点后跳出循环。
        num_dec += 1
    num_i=int(round((math.log(val_resistance,10)-num_dec)*int(lis_eia[num_id]),0))        #求公式中的i,四舍五入，并转成整型

    lis_value = adjacent_value(num_dec,num_i,num_id)        #计算当前值预估位置的相邻值，用于比较判断

    for val in [0,1,2]:
        if float(val_resistance) < lis_value[val]*(1+lis_jd[num_id]) and float(val_resistance) > lis_value[val]*(1-lis_jd[num_id]):
            lis_value = adjacent_value(num_dec,(num_i-1+val),num_id)
            break
    return lis_value
