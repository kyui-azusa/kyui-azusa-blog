# example3_2.py
# coding=utf-8

t = int(input("请输入年份:"))

if t % 400 == 0 or (t % 4 == 0 and t % 100 != 0):
    print(t, '年是闰年', sep='')
else:
    print(t, '年不是闰年', sep='')
