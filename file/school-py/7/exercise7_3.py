# exercise7_3.py
# coding=utf-8

list1 = [20, 99, 88, 79, 59, 43, 23, 90, 44, 89]
list2 = [25, 91, 82, 72, 51, 46, 28, 98, 42, 87]

for i in list2:
    if i % 2 == 0:
        list1.append(i)
print('新的list1::', list1)