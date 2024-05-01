#exercise9_1.py
#coding:utf-8

dict1 = {
    "张三":45,
    "李四":78,
    "徐来":40,
    "沙思思":96,
    "如一":65,
    "司音":90,
    "赵敏":78,
    "张旭宁":99,
    "柏龙":60,
    "思琪":87,
}
s = 0
for key in dict1:
    print(f'{key}\t{dict1[key]}')
    s += dict1[key]
print(f'全班共有{len(dict1)}人,平均成绩为{s/len(dict1):.2f}分')