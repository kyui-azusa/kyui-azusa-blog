# example4_2.py
# coding=utf-8

print('list1:')
list1=[]
for i in range(4):
    list1.append(int(input(f'请输入第{i+1}个整数: ')))
print('list2:')
list2=[]
for i in range(3):
    list2.append(int(input(f'请输入第{i+1}个整数: ')))
print(list1)
print(list2)
list1.extend(list2)
print(f'列表list2合并到list1中后的数据: {list1}')
list1.extend([90,100])
print(f'加上90,100后的1ist1的数据: {list1}')
list1.sort(reverse=True)
print(f'降序排列后最终列表list1中的数据: {list1}')