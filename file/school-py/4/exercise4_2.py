# exercise4_2.py
# coding=utf-8

r = 177777777802222222005

if r % 18 == 0 or (r + 15) % 18 == 0:
    print(r, '是符合要求的数字', sep='')
else:
    print(r, '不是符合要求的数字', sep='')
