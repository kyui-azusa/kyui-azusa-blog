#exercise9_2.py
#coding:utf-8
list1 = [2.3, 4.5, 24, 17, 1, 7.8, 39, 21, 0.5, 1.2, 4, 1, 0.3]
dict1 = {
    'paltinum':0,
    'gold':0,
    'silver':0,
    'ordinary':0,
}
for i in list1:
    if i >= 10:
        dict1['paltinum'] += 1
    elif i >= 5:
        dict1['gold'] += 1
    elif i >= 3:
        dict1['silver'] += 1
    else:
        dict1['ordinary'] += 1
print(dict1)