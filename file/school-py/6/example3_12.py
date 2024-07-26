# example3_12.py
# coding=utf-8

sales = [5000, 3000, 8000, 10600, 6000, 5000]  
found = 0 
for i in sales:  
    if i >= 6000:  
        print("第一个大于或等于6000的销售额是:", i)  
        found = 1
        break  
if not found:
    print('未找到。')