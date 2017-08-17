# encoding:utf-8
import re
import string

s = ['黄/ATT 师傅/SBV 来电/SBV 咨询/COO 取消/COO 订单/VOB 已/ADV 告知/HED 需要/VOB 拨打/VOB 客服/SBV 按/VOB 号键/VOB 。/WP',
     '白/ATT 师傅/ATT 来电/ATT 咨询/ATT 订单/VOB 状态/SBV 已/ADV 告知/HED 乘客/DBL 已经/ADV 取消/VOB 。/WP',
     '胡/ATT 师傅/SBV 来电/HED 咨询/COO 取消/COO 订单/VOB 已/ADV 告知/COO 需要/VOB 拨打/VOB 客服/SBV 按/VOB 号键/VOB 。/WP']

# def sytax_out(contents):
#     wordsList = []
#     for content in contents:
#         content = content.split()
#         new_content = []
#         for i in content:
#             if re.search(r'/VOB',i) or re.search(r'/ADV',i) or re.search(r'/ATT',i):
#                 new_content.append(i)
#         file_string = ' '.join(new_content)
#         file_string = re.sub(r'/[\w]+','',file_string)
#         wordsList.append(file_string)
#     return wordsList

def sytax_out(contents):
    wordsList = []
    for content in contents:
        content = content.split()
        new_content = []
        for i in range(len(content)):
            if len(content) - i>1:
                if re.search(r'/COO',content[i]) and re.search(r'/VOB',content[i+1]):
                    content[i] = content[i] + content[i+1]
                    content[i+1] = content[i+1] +'/WP'
                    new_content.append(content[i])
                # elif re.search(r'/COO',content[i]) and re.search(r'/ATT',content[i+1]):
                #     content[i] = content[i] + content[i+1]
                #     content[i + 1] = content[i + 1] +'/WP'
                #     new_content.append(content[i])
                elif re.search(r'/ATT',content[i]) and re.search(r'/VOB',content[i+1]):
                    content[i] = content[i] + content[i+1]
                    content[i + 1] = content[i + 1] +'/WP'
                    # if content[i+2]:
                    #     if re.search(r'/SBV',content[i+2]):
                    #         content[i] = content[i] + content[i+2]
                    #         content[i + 2] = content[i + 2] + '/WP'
                    new_content.append(content[i])
                elif not re.search(r'/WP',content[i]):
                    new_content.append(content[i])
            elif not re.search(r'/WP', content[i]):
                new_content.append(content[i])
        file_string = ' '.join(new_content)
        file_string = re.sub(r'/[\w]+','',file_string)
        wordsList.append(file_string)
    return wordsList

# k = sytax_out(s)
# for i in k:
#     print i