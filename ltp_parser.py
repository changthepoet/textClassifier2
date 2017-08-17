# encoding:utf-8
from pyltp import Parser, Segmentor, Postagger

s = ['司机13318757313来电表示提现未到帐，已告知会有延迟到账的现象','司机来电咨询订单状态 已告知乘客取消订单。','司机来电表示乘客飞机晚点，询问等待费用的情况，坐席已告知。']

def ltp_parser(strli):
    segmentor = Segmentor()  # 初始化实例
    postagger = Postagger()  # 初始化实例
    parser = Parser()  # 初始化实例
    segmentor.load('models/cws.model')  # 加载模型
    postagger.load('models/pos.model')  # 加载模型
    parser.load('models/parser.model')  # 加载模型
    new_strli = []
    for str in strli:
        words = segmentor.segment(str)  # 分词
        postags = postagger.postag(words)  # 词性标注
        arcs = parser.parse(words, postags)  # 句法分析
        rel = []
        head = []
        for arc in arcs:
            rel.append(arc.relation)
            head.append(arc.head)
        pstr =  " ".join("%s/%s/%s" % it for it in zip(list(words), rel,head))
        new_strli.append(pstr)
    parser.release()# 释放模型
    segmentor.release()  # 释放模型
    postagger.release()  # 释放模型
    return new_strli

# k = ltp_parser(s)
# for t in k:
#     print t