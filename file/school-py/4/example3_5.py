# example3_5.py
# coding=utf-8

Ctype = int(input("请输入客户类型(小于5为新客户):"))
Price = eval(input("请输入标准价格:"))
Quantity = eval(input("请输入订货数量:"))

if Ctype > 0 and Price > 0 and Quantity > 0:
    if Ctype < 5:
        if Quantity < 800:
            Coff = 0
        else:
            Coff = 0.02
    else:
        if Quantity < 500:
            Coff = 0.03
        elif Quantity < 1000:
            Coff = 0.05
        elif Quantity < 2000:
            Coff = 0.08
        else:
            Coff = 0.1
    
    Pays = Quantity * Price * (1 - Coff)
    print("应付款为:", Pays)
else:
    print("输入错误。")
