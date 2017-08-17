# encoding:utf-8
import re
import string

import pandas as pd
stopwords = [line.rstrip() for line in open('text/stopword2.txt')]
df=pd.read_excel('excel/d1.xlsx')
t = df.stopMove.tolist()

stopwords1 = []
for i in stopwords:
    stopwords1.append(i.decode('utf-8'))

def fileWordProcess(contents):
    wordsList = []
    # delEStr  = string.punctuation+' '+string.digits
    # identify = string.maketrans('','')
    # contents = re.sub(r'\s+',' ',contents) # trans多空格to空格
    # contents = re.sub(r'\n',' ',contents) # trans换行to空格
    # contents = re.sub(r'\t',' ',contents) # trans Tab to空格
    # contents = contents.translate(identify, delEStr)
    for seg in contents:
        if seg not in stopwords1:# remove 停用词  
            if seg!=' ': # remove 空格  
                wordsList.append(seg) # create 文件词列表  
    file_string = ' '.join(wordsList)
    file_string = re.sub(r'[\w]+','',file_string)
    file_string = re.sub(string.digits,'',file_string)
    return file_string
t2 = []
for x in t:
    x = str(x)
    x = x.split()
    x2 = fileWordProcess(x)
    t2.append(x2)
df['stopMove'] = t2
writer = pd.ExcelWriter('excel/d1.xlsx')
df.to_excel(writer,'sheet2')
writer.save()

# delEStr = string.punctuation + ' ' + string.digits
# identify = string.maketrans('','')