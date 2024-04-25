#exercise8_1.py
#coding=utf-8
list1 = []

print('请输入数字构建一个包含10个奇数的列表')
while len(list1) < 10:
    a = int(input('请输入数字:'))
    if int(a) % 2 == 1:
        list1.append(int(a))
    else:
        print('输入的不是奇数!!!')    
print('列表为:\t',list1)
print('和:\t',sum_1:=sum(list1))
print('平均值:\t',sum_1/10)