# exercise6_5.py
# coding=utf-8

print('打印出 1\~100 之间能被7整除，但不能同时被5整除的所有数：')
for i in range(7, 101,7):
    if i % 5 != 0:
        print(i, end='\t')