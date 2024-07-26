# example3_15.py
# coding=utf-8

print(f'所有三位数的素数如下:',end='\t')
for i in range(100,1001):
    k = 0    
    for j in range(2,int(i/2+1)):
        if i % j ==0:
            k = 1
            break
    if k == 0:
        print(i,end='\t')