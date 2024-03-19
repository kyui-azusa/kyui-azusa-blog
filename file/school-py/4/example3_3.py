# example3_3.py
# coding=utf-8

jobSeeker_info = {
    'age':24,
    'major':'投资银行',
    'if_key':'false',
    'exp':3,
}

def in_notice(info):#Interview Notice
    if info['age']<=25 and info['major']=='金融工程' and info['if_key']=='true' or info['major']=='投资银行' and info['exp']>=3:
        print('面试通知')

in_notice(jobSeeker_info)