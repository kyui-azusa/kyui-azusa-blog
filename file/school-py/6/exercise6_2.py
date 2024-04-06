# exercise6_2.py
# coding=utf-8

print('三位数中所有水仙花数是:')
for num in range(100,1000):
    s = 0
    for i in str(num):
        s += int(i)**3
    if s == num:
        print(num,end='\t')