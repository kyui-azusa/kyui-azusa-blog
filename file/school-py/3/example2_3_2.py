#-- codeing=utf-8 --
#@File:example2_3_2.py

number = input('请输入股票代码:')
name = input('请输入股票名称:')
highest = float(input('请输入当天最高价:'))
lower = float(input('请输入当天最低价:'))
diff = highest - lower
print("股票代码+股票名称:" + number + "+" + name)
print("最高价:", highest, "最低价:", lower, "差值:", diff, sep="")