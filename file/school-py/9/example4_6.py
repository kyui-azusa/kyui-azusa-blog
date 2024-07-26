#example4_6.py
#coding=utf-8

info = {  
    '601398': ['工商银行', 5.51],
    '000001': ['平安银行', 8.94],
    '601939': ['建设银行', 6.89],
    '601328': ['交通银行', 5.61],
}

no = input("请输入编号:")
while no in info:
    print(info[no])
    no = input("请输入编号:")
else:
    print("无查询结果!")