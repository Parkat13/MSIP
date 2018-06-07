# -*- coding: utf-8 -*-
import sys
import codecs
import string
import numpy as np
import copy
import math
from main import morph_anal
from nltk.tokenize import sent_tokenize
reload(sys)
sys.setdefaultencoding('utf-8')
f_q = codecs.open('MSIP-3(q).txt', 'r', 'utf8')
f_doc = codecs.open('MSIP-3(doc).txt', 'r', 'utf8')
f_result_idf = open('MSIP-3(result_idf).txt', 'w')
f_result_not_idf = open('MSIP-3(result_not_idf).txt', 'w')
q = f_q.read()
col = f_doc.read()
doc = sent_tokenize(col)
dict = {}
doc_ = copy.deepcopy(doc)
doc_.append(q)
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
    vec.append([])
    for j in dict:
        vec[i].append(dict[j])
        if dict[j] != 0:
            vec_all[len(vec[i]) - 1] += 1
        dict[j] = 0
    vec[i] = np.asarray(vec[i])

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
q_vect = np.asarray(q_vect)

vec1 = copy.deepcopy(vec)
q_vect1 = copy.deepcopy(q_vect)

### Без учета idf

#    Нормализация векторов
for i in range(len(vec1)):
    if np.sum(vec1[i]**2) != 0.0:
        vec1[i] = vec1[i] / (1.0 * np.sqrt(np.sum(vec1[i]**2)))
q_vect1 = q_vect1 / (1.0 * np.sqrt(np.sum(q_vect1**2)))

#    Вычисление сходства документов с запросом
res_cos = []
for i in range(len(vec1)):
    res_cos.append([np.sum(vec1[i] * q_vect1),i])

#    Сортировка документов по наибольшему сходству и вывод в файл
for i in range(len(res_cos)):
    for j in range(i-1, -1, -1):
        if res_cos[j + 1][0] > res_cos[j][0]:
            res_cos[j + 1], res_cos[j] = res_cos[j], res_cos[j + 1]

for i in range(len(res_cos)):
    f_result_not_idf.write(str(res_cos[i][0]) + ' ' + str(doc[res_cos[i][1]]) + '\n')


### С учетом idf
#    Определение весов для каждого слова каждого документа
for i in range(len(vec)):
    for j in range(len(vec[i])):
        vec[i][j] = vec[i][j] * math.log10(len(doc) / (1.0 + vec_all[j]))
        #vec[i][j] = vec[i][j] * vec_all[j]

#    Нормализация векторов
for i in range(len(vec)):
    if np.sum(vec[i]**2) != 0.0:
        vec[i] = vec[i] / (1.0 * np.sqrt(np.sum(vec[i]**2)))
q_vect = q_vect / (1.0 * np.sqrt(np.sum(q_vect**2)))

#    Вычисление сходства документов с запросом
res_cos = []
for i in range(len(vec)):
    res_cos.append([np.sum(vec[i] * q_vect),i])

#    Сортировка документов по наибольшему сходству и вывод в файл
for i in range(len(res_cos)):
    for j in range(i-1, -1, -1):
        if res_cos[j + 1][0] > res_cos[j][0]:
            res_cos[j + 1], res_cos[j] = res_cos[j], res_cos[j + 1]

for i in range(len(res_cos)):
    f_result_idf.write(str(res_cos[i][0]) + ' ' + str(doc[res_cos[i][1]]) + '\n')
f_q.close()
f_doc.close()
f_result_idf.close()
f_result_not_idf.close()
