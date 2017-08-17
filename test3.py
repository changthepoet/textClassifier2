# coding=utf-8
import re
import string

import pandas as pd
import chardet

s = ['司机13318757313来电表示提现未到帐，已告知会有延迟到账的现象','司机来电咨询订单状态 已告知乘客取消订单。','司机来电表示乘客飞机晚点，询问等待费用的情况，坐席已告知。']

df=pd.read_excel('excel/split_train.xlsx')
t = df.stopMove.tolist()

def wordfilter(contents):
    new_contents = []
    # delEStr = string.punctuation+' '+string.digits
    # identify = string.maketrans('','')
    for content in contents:
        content = content.encode('utf8')
        content = re.sub(r'\s+',' ',content) # trans多空格to空格
        content = re.sub(r'\n',' ',content) # trans换行to空格
        content = re.sub(r'\t',' ',content) # trans Tab to空格
        content = content.replace(string.punctuation,'')
        # content = content.translate(identify, delEStr)
        new_contents.append(content)
    return new_contents

df['stopMove'] = wordfilter(t)
writer = pd.ExcelWriter('excel/split_train1.xlsx')
df.to_excel(writer,'sheet2')
writer.save()
