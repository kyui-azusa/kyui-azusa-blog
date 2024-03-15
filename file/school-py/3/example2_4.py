#-- codeing=utf-8 --
#@File:example2_4.py

import math

a = float(input("请输入复数的实部："))
b = float(input("请输入复数的虚部："))
r = math.sqrt(a ** 2 + b ** 2)

print('输入的复数为:',a,'+',b,'j',sep='')
print('复数的模为:',r,sep='')