# exercise4_1.py
# coding=utf-8

score = int(input("请输入百分制成绩（0\~100）："))

if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
else:
    print('E')
