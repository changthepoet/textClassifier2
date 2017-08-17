# encoding:utf-8
from __future__ import unicode_literals

from bosonnlp import BosonNLP


def wordsplit(a):
    nlp = BosonNLP('F0M7mzYq.14685.YvqU_Dxkya99')
    result = nlp.tag(a)
    b = []
    for d in result:
        b.append(' '.join("%s" % it for it in d['word']))
    return b
