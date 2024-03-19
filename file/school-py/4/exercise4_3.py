# exercise4_3.py
# coding=utf-8

import math

a = 8
b = 18
sita = 45
c = math.sqrt(a**2+b**2-2*a*b*math.cos(math.radians(sita)))
print(f'第三边长度为{c}')