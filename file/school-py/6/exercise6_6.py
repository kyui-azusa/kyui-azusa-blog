# exercise6_6.py
# coding=utf-8

for score in range(100):
    if score >= 85:
        grade = "优秀"
    elif score >= 70:
        grade = "中等"
    elif score >= 60:
        grade = "及格"
    else:
        grade = "不及格"
    print('成绩:', score, '等级:', grade)