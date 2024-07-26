#example4_1.py
#coding=utf-8
list1 = list(range(10, 0, -1))
print("原来序列：", list1)

list2 = list1[::2]
list2.sort()
list1[::2] = list2
print("偶数下标升序：", list1)