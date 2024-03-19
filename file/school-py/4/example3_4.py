# example3_4.py
# coding=utf-8

price = eval(input("请输入标准价格:"))
Quantity = eval(input("请输入订货量:"))

if Quantity < 0 or price < 0:
    print("输入的订货量与标准价格均不能小于0!")
else:
    if Quantity < 300:
        Coff = 0.0
    elif Quantity < 500:
        Coff = 0.03
    elif Quantity < 1000:
        Coff = 0.05
    elif Quantity < 2000:
        Coff = 0.08
    else:
        Coff = 0.1
    
    print("折扣率为:", Coff)
    Pays = Quantity * price * (1 - Coff)
    print("支付金额:", Pays)
