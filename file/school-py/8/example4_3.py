#example4_3.py
#coding=utf-8
data = [12.04, 11.15, 13.47, 13.58, 12.04, 12.04, 11.15, 12.58, 11.15]
  
print("共有" + str(len(data)) + "个数据，分别为:", data)
print("收盘价为12.04元的次数:", data.count(12.04))
x = min(data)
print("收盘价中最小数据:", x)
data.remove(x)
print("删除首次出现的最小数据后的列表:", data)