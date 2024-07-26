# exercise7_2.py
# coding=utf-8

scores = [68, 75, 32, 99, 78, 45, 88, 72, 83, 78]
grade = [0, 0, 0, 0]

for score in scores:
    if 90 <= score <= 100:
        grade[0] += 1
    elif 80 <= score < 90:
        grade[1] += 1
    elif 60 <= score < 80:
        grade[2] += 1
    else:
        grade[3] += 1

for grade, count in zip(['优', '良', '中', '差']  , grade):
    print(f"{grade}等级的人数：{count}")