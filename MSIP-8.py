# -*- coding: utf-8 -*-
import sys
import codecs
import numpy as np
import copy
import math
from main import morph_anal
reload(sys)
sys.setdefaultencoding('utf-8')
a = '-t'
if a == '-s':
    f_doc = codecs.open('MSIP-8(study).txt', 'r', 'utf8')
    f_dict = open('MSIP-8(dict).txt', 'w')
    dict_all = {}
    dict_c = [{},{},{}]
    doc = f_doc.readline().lower().split()
    while len(doc) != 0:
        n = 0
        if doc[0] == '1':
            n = 0
        elif doc[0] == '2':
            n = 1
        else:
            n = 2
        f_input = open('MSIP-2(text).txt', 'w')
        f_input.write(' '.join(doc[1:]))
        f_input.close()
        morph_anal()
        f_output = codecs.open('MSIP-2(result).txt', 'r', 'utf8')
        text = f_output.read().split()
        for j in (range(len(text) / 2)):
            if text[2*j] in dict_all:
                dict_all[text[2*j]] += float(text[2 * j + 1])
            else:
                dict_all[text[2*j]] = float(text[2 * j + 1])
            if text[2*j] in dict_c[n]:
                dict_c[n][text[2*j]] += float(text[2 * j + 1])
            else:
                dict_c[n][text[2*j]] = float(text[2 * j + 1])
        f_output.close()
        doc = f_doc.readline().lower().split()
    voc = len(dict_all)
    f_dict.write(str(voc) + '\n')
    p1 = 10.0/30.0
    p2 = 10.0/30.0
    p3 = 10.0/30.0
    n1 = 0
    n2 = 0
    n3 = 0
    for i in dict_c[0]:
        n1 += dict_c[0][i]
    for i in dict_c[1]:
        n2 += dict_c[1][i]
    for i in dict_c[2]:
        n3 += dict_c[2][i]
    f_dict.write(str(p1) + ' ' + str(n1) + '\n')
    for i in dict_c[0]:
        f_dict.write(i + ' ' + str(dict_c[0][i]) + ' ')
    f_dict.write('\n' + str(p2) + ' ' + str(n2) + '\n')
    for i in dict_c[1]:
        f_dict.write(i + ' ' + str(dict_c[1][i]) + ' ')
    f_dict.write('\n' + str(p3) + ' ' + str(n3) + '\n')
    for i in dict_c[2]:
        f_dict.write(i + ' ' + str(dict_c[2][i]) + ' ')
    f_dict.write('\n')
    f_doc.close()
    f_dict.close()
elif a == '-t':
    f_q = codecs.open('MSIP-8(test).txt', 'r', 'utf8')
    f_dic = codecs.open('MSIP-8(dict).txt', 'r', 'utf8')
    f_result = open('MSIP-8(result).txt', 'w')
    voc = float(f_dic.readline())
    q = f_dic.readline().split()
    p1 = float(q[0])
    n1 = float(q[1])
    c1 = f_dic.readline().split()
    q = f_dic.readline().split()
    p2 = float(q[0])
    n2 = float(q[1])
    c2 = f_dic.readline().split()
    q = f_dic.readline().split()
    p3 = float(q[0])
    n3 = float(q[1])
    c3 = f_dic.readline().split()
    q = f_q.read().lower()
    dict_c1 = {}
    dict_c2 = {}
    dict_c3 = {}
    for j in (range(len(c1) / 2)):
        dict_c1[c1[2 * j]] = float(c1[2 * j + 1])
    for j in (range(len(c2) / 2)):
        dict_c2[c2[2 * j]] = float(c2[2 * j + 1])
    for j in (range(len(c3) / 2)):
        dict_c3[c3[2 * j]] = float(c3[2 * j + 1])
    dict = {}
    f_input = open('MSIP-2(text).txt', 'w')
    f_input.write(q)
    f_input.close()
    morph_anal()
    f_output = codecs.open('MSIP-2(result).txt', 'r', 'utf8')
    text = f_output.read().split()
    for j in (range(len(text) / 2)):
        dict[text[2 * j]] = float(text[2 * j + 1])
    f_output.close()
    for j in dict:
        if j in dict_c1:
            p1 = p1 * (dict_c1[j] + 1.0)/(n1 + voc)
        else:
            p1 = p1 * 1.0/(n1 + voc)
        if j in dict_c2:
            p2 = p2 * (dict_c2[j] + 1.0)/(n2 + voc)
        else:
            p2 = p2 * 1.0/(n2 + voc)
        if j in dict_c3:
            p3 = p3 * (dict_c3[j] + 1.0)/(n3 + voc)
        else:
            p3 = p3 * 1.0/(n3 + voc)
    p = [p1, p2, p3]
    p.sort()
    p.reverse()
    for i in p:
        if p1 == i:
            f_result.write('Политика ' + str(p1) + '\n')
        elif p2 == i:
            f_result.write('Технологии и наука ' + str(p2) + '\n')
        else:
            f_result.write('Культура ' + str(p3) + '\n')
    f_dic.close()
    f_q.close()
    f_result.close()
else:
    print 'Error\n'

