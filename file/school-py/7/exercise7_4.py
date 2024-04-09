# exercise7_4.py
# coding=utf-8

scores = [100, 90, 45, 200, 67, 82, 91, 39, 78, 34, -49, 20, 99, 88, 79, 59, 43, 23, 90, 44, 89]
for score in scores:
    if score > 100 or score < 0:
        grade = '成绩错误'
    else:
        if score >= 85:
            grade = "优良"
        elif score >= 70:
            grade = "中等"
        elif score >= 60:
            grade = "及格"
        else:
            grade = "不及格"
    print('成绩:', score, '\t', grade)