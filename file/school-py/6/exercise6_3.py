# exercise6_3.py
# coding=utf-8

num = 7
i = int(input('请输入您猜的数(0~9): '))
while i != num:
    if i < num:
        print('太小')
    if i > num:
        print('太大')
else:
    print('恭喜!你猜中了!')