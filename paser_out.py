# encoding:utf-8
import re
import string

import pandas as pd
stopwords = [line.rstrip() for line in open('text/stopword2.txt')]
df=pd.read_excel('excel/paser.xlsx')
t = df.content.tolist()

stopwords1 = []
for i in stopwords:
    stopwords1.append(i.decode('utf-8'))

def fileWordProcess(contents):
    wordsList = []
    # contents = re.sub(r'\s+','',contents) # trans多空格to空格
    # contents = re.sub(r'\n',' ',contents) # trans换行to空格
    # contents = re.sub(r'\t',' ',contents) # trans Tab to空格
    # contents = contents.translate(identify, delEStr)
    for seg in contents:
        if re.search(ur"/",seg):# remove 停用词  
            if seg!=' ': # remove 空格  
                wordsList.append(seg) # create 文件词列表  
    file_string =' '.join(wordsList)
    return re.sub('[\w]+','',file_string)
t2 = []
for x in t:
    x1 = x.split()
    x2 = fileWordProcess(x1)
    t2.append(x2)
df['parserOut'] = t2
writer = pd.ExcelWriter('excel/paser_out.xlsx')
df.to_excel(writer,'sheet2')
writer.save()

# delEStr = string.punctuation + ' ' + string.digits
# identify = string.maketrans('','')