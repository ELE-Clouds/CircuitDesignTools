#!/usr/bin/
# -*- coding: utf-8 -*-
'''
*************************************************
  文件名：srvc_mod
  Copyright (C), 2016, ELE-Clouds.All rights reserved.
  作者：ELE-Clouds
  日期：2016年12月15日
  版本：V0.01
  描述: 
        本程序主要用于计算输入值所在的范围属于哪个 EIA 系列标准电阻值。

  主要函数列表:   //每条记录应包括函数名及功能简要说明
    1. adjacent_value(num_n,num_i,num_id,str_formula='2')
        通过给定的参数，计算出某一个EIA标准值的左右相邻的值。

    2. val_Srv(val_resistance,num_id,str_formula='2')
        通过给定参数计算并判断出给定值匹配的EIA标准值

  修改历史记录：: //每条修改记录应包括修改日期、修改者及修改内容简述
    1.修改日期:
       修改人:
       修改内容:
    2. ....
*************************************************
'''

import math

'''
*************************************************
  函数名称：adjacent_value        # 函数名称
  描述:                           # 函数功能、性能等的描述
      根据给定参数计算出指定值相邻的2个值，并存到列表中，然后返回。

  调用函数：             // 被本函数调用的函数清单
      round()
      float()
      log()
      append()

  被调用函数：          // 调用本函数的函数清单
      val_Srv(val_resistance,num_id,str_formula='2')

  访问表:               // 被访问的表（此项仅对于牵扯到数据库操作的程序）
  修改表:               // 被修改的表（此项仅对于牵扯到数据库操作的程序）
  输入参数:              
      num_n              整型变量，起始值为0。EIA基础值的倍率，即，1后面有几个0。
      num_i              整型变量，起始值为0。起索引作用，主要表示标准值所在精度范围内的“标准值列表”中的位置。
      num_id             整型变量，起始值为0。用于传递EIA标准号（精度代号）所在list中的索引值，方便后续对其及相关参数的调用。
      str_formula='2'    字符串变量，用于对公式字典变量内容进行选择，范围（'0','1','2'），分别对应不同的公式。
                        
  输出参数:               // 对输出参数的说明。

  返回值:                  // 函数返回值的说明
      li_value           list变量，用于存放计算出来的指定值及比它小和比它大的值。

  其它说明:               // 其它说明
    # 以下为要用到的math函数
    # math.log(值,底数)  eg. 求2自乘了几次等于8， math.log(8,2)
    # math.sqrt(值)  开平方  eg. math.sqrt(16) 结果是：4.0
    # x**(1/n)：表示求 开x的n方根。  eg.  8**(1.0/3)  求8的3次方根，结果为2.  注意：括号内必须有一个数为浮点数，即整数后加".0"。 
    # 其它函数：
    # round(值,小数位数)   对值保留一定的小数位数，并进行四舍五入。
*************************************************
'''
def adjacent_value(num_n,num_i,num_id,str_formula='2'): 
    lis_eia = [6,12,24,48,96,192]
    lis_gbDec = [2,2,2,3,3,3]    #标准值保留的小数位数
    li_value = []
    li_adj = [-1,0,1]    #相邻值相对当前值的位置，比其小的用“-1”，比其大的用“+1”，本身为0.

    for num in li_adj:
        #计算公式选择字典
        dic_formula1={'0':((10**(num_n))*round(10**((num_i+num)/float(lis_eia[num_id])),lis_gbDec[num_id]-1)),                        #Val=d*10**(i/N)
        '1':((10**(num_n))*round(math.exp((((num_i+num)-1)/float(lis_eia[num_id]))*math.log(10,math.e)),(lis_gbDec[num_id]-1))),      #指数式公式
        '2':((10**(num_n))*round(round(10**(1/float(lis_eia[num_id])),lis_gbDec[num_id])**(num_i+num),lis_gbDec[num_id]-1))}          #Val = 10n × (N√10)(0,1,2……N-1)
        
        li_value.append(dic_formula1[str_formula])
    return li_value



'''
*************************************************
  函数名称：val_Srv               # 函数名称
  描述:                           # 函数功能、性能等的描述
      根据给定的值及精度范围，计算并推断出给定值所匹配的标准值。
      根据公式倒推出给定值所在标准值列表中的预估位置，然后根据预估位置，
      调用adjacent_value函数，计算出当前位置的标准值及左右相邻的2个值，
      再用计算出的值根据所选精度范围来判断出给定值所在的范围属于哪个标准值，
      最后，再利用符合要求标准值的信息计算出最终的标准值及与其左右相邻的2个
      值，并返回，用于GUI界面中的显示。

  调用函数：             // 被本函数调用的函数清单
      adjacent_value(num_n,num_i,num_id,str_formula='2')

  被调用函数：          // 调用本函数的函数清单
      clickMe()

  访问表:               // 被访问的表（此项仅对于牵扯到数据库操作的程序）
  修改表:               // 被修改的表（此项仅对于牵扯到数据库操作的程序）
  输入参数:               
      val_resistance     浮点型变量，用于传递用户输入的值。
      num_id             整型变量，起始值为0。起索引作用，主要标示用户选择的经度值所在列表的位置，该列表与EIA系列好列表对应。
      str_formula='2'    字符串变量，主要用于程序员根据需要选择不同的公式。默认选择位置2。

  输出参数:               // 对输出参数的说明。
  返回值:
      lis_value          list变量，用于存放计算出来的指定值及比它小和比它大的值，即最终结果。

  其它说明:
    # 以下为要用到的math函数
    # math.log(值,底数)  eg. 求2自乘了几次等于8， math.log(8,2)
    # math.sqrt(值)  开平方  eg. math.sqrt(16) 结果是：4.0
    # x**(1/n)：表示求 开x的n方根。  eg.  8**(1.0/3)  求8的3次方根，结果为2.  注意：括号内必须有一个数为浮点数，即整数后加".0"。 
    # 其它函数：
    # round(值,小数位数)   对值保留一定的小数位数，并进行四舍五入。
*************************************************
'''
def val_Srv(val_resistance,num_id,str_formula='2'):
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
    num_dec -= 1     #原值从1开始，需求：从零开始。
    val_temp = round(val_resistance*(10**(-(num_dec))),1)

    #计算公式选择字典
    dic_formula2={'0':int(round((math.log(val_temp,10))*int(lis_eia[num_id]),0)),                   #求公式中的i,四舍五入，并转成整型，似乎用于val=d**n*10**(i/N)
    '1':int(round((((math.log(val_temp,math.e)*lis_eia[num_id])/math.log(10,math.e))+1),0)),        #求公式中的i,四舍五入，并转成整型,适用于指数公式的反向推导
    '2':int(round(math.log(val_temp,10**(1.0/lis_eia[num_id]))))}                                   #求公式中的i,四舍五入，并转成整型,适用于开方公式的反向推导
    
    num_i = dic_formula2[str_formula]    
    
    lis_value = adjacent_value(num_dec,num_i,num_id)                                                #计算当前值预估位置的相邻值，用于比较判断

    #数值区域判断
    for val in [0,1,2]:
        if float(val_resistance) < lis_value[val]*(1+lis_jd[num_id]) and float(val_resistance) > lis_value[val]*(1-lis_jd[num_id]):
            lis_value = adjacent_value(num_dec,(num_i-1+val),num_id)
            break
    return lis_value
