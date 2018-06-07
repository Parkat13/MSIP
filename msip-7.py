# -*- coding: utf-8 -*-
import sys
import codecs
import numpy as np
import copy
import math
from main import morph_anal
from nltk.tokenize import sent_tokenize
reload(sys)
sys.setdefaultencoding('utf-8')
f_q = codecs.open('MSIP-7(q).txt', 'r', 'utf8')
f_doc = codecs.open('MSIP-7(doc).txt', 'r', 'utf8')
f_result = open('MSIP-7(result).txt', 'w')
q = f_q.read()
col = f_doc.read()
doc = sent_tokenize(col)
dict = {}
doc_ = copy.deepcopy(doc)
doc_.append(q)
dict_res = {}
#    Определение слов в словаре(сколько и какие слова будут в векторах)
for i in range(len(doc_)):
    f_input = open('MSIP-2(text).txt', 'w')
    f_input.write(doc_[i])
    f_input.close()
    morph_anal()
    f_output = codecs.open('MSIP-2(result).txt', 'r', 'utf8')
    text = f_output.read().split()
    for j in (range(len(text) / 2)):
        dict[text[2*j]] = float(text[2*j+1])
    f_output.close()

vec_all = []
for i in dict:
    vec_all.append(0)
    dict[i] = 0

#    Определение векторов для каждого документа
vec = []
for i in range(len(doc)):
    f_input = open('MSIP-2(text).txt', 'w')
    f_input.write(doc[i])
    f_input.close()
    morph_anal()
    f_output = codecs.open('MSIP-2(result).txt', 'r', 'utf8')
    text = f_output.read().split()
    for j in (range(len(text) / 2)):
        dict[text[2*j]] = float(text[2*j + 1])
    f_output.close()
    dict_res[doc[i]] = []
    for j in dict:
        dict_res[doc[i]].append(dict[j])
        if dict[j] != 0:
            vec_all[len(dict_res[doc[i]]) - 1] += dict[j]
        dict[j] = 0

#    Определение вектора запроса
f_input = open('MSIP-2(text).txt', 'w')
f_input.write(q)
f_input.close()
morph_anal()
f_output = codecs.open('MSIP-2(result).txt', 'r', 'utf8')
text = f_output.read().split()
for j in (range(len(text) / 2)):
    dict[text[2*j]] = float(text[2*j + 1])
f_output.close()
q_vect = []
for j in dict:
    q_vect.append(dict[j])

all_sum = sum(vec_all[j] for j in range(len(vec_all)))
###
for i in dict_res:
    s = sum(dict_res[i][j] for j in range(len(dict_res[i])))
    if s == 0:
        dict_res[i] = 0.0
    else:
        c = list(math.log(1.0 + ((0.5*dict_res[i][j])/(1.0*s) + (0.5*vec_all[j])/(1.0 *all_sum))) for j in range(len(q_vect)) if q_vect[j]!=0)
        dict_res[i] = 0.0
        for j in c:
            dict_res[i] += j
for i in sorted(dict_res, key=dict_res.__getitem__, reverse=True):
    f_result.write(str(dict_res[i]) + ' ' + str(i) + '\n')

f_q.close()
f_doc.close()
f_result.close()

