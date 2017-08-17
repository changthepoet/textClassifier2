# encoding:utf-8
import re
import string
import pandas as pd
# from ltp_parser import ltp_parser
# from ltp_parser2 import ltp_parser2
from ltp_parser3 import ltp_parser3
df = pd.read_excel('excel/a1.xlsx')
t = df.content.tolist()
u = []
for a in t:
    a = str(a)
    a = a.encode('utf8')
    a = re.sub(r'\s+',' ',a) # trans多空格to空格
    a = re.sub(r'\n',' ',a) # trans换行to空格
    a = re.sub(r'\t',' ',a) # trans Tab to空格
    a = a.strip(string.punctuation)
    a = a.strip()
    if '。' not in a or not a.endswith('。'):
        a = a + '。'
    u.append(a)
spliter = ltp_parser3(u)
df['stopMove'] = spliter
writer = pd.ExcelWriter('excel/d1.xlsx')
df.to_excel(writer,'sheet1')
writer.save()