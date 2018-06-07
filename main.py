# -*- coding: utf-8 -*-
def f(x): return (x.isalpha()) or (x.isspace())

def morph_anal():
    import sys
    import codecs
    import pymorphy2
    import string
    morph = pymorphy2.MorphAnalyzer()
    reload(sys)
    sys.setdefaultencoding('utf-8')
    f_open = codecs.open('MSIP-2(text).txt', 'r', 'utf8')
    f_result = open('MSIP-2(result).txt', 'w')
    dict = {}
    text = f_open.readline()
    while text != '':
        words = ''.join(filter(f, text)).lower().split()
        for i in range(len(words)):
            word = morph.parse(words[i])[0].normal_form
            if word in dict :
                dict[word] += 1
            else:
                dict[word] = 1
        text = f_open.readline()
    #dict = sorted(dict.values())
    for i in sorted(dict, key=dict.__getitem__, reverse=True):
        f_result.write(str(i) + ' ' + str(dict[i]) + '\n')
    f_open.close()
    f_result.close()
