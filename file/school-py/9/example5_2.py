#example5_2.py
#coding=utf-8

for i in range(1, 10):
    for j in range(1, i + 1):
        print("{}*{}={:<4d}".format(i, j, i * j), end='')
    print()