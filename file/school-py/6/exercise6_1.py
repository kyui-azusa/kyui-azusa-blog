# exercise6_1.py
# coding=utf-8

s = 0
print('1000以内素数:')
for i in range(2,1001):
    k = 0    
    for j in range(2,int(i/2+1)):
        if i % j ==0:
            k = 1
            break
    if k == 0:
        s += i
        print(i,end='\t')
print(f'\n1000以内素数之和:\t{s}')