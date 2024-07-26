# exercise7_1.py
# coding=utf-8

nums = []
i = int(input('请输入数字,以-1结束: '))
while i != -1:
    nums.append(i)
    i = int(input('请输入数字: '))
print(nums)