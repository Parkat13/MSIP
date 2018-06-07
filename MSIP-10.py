# -*- coding: utf-8 -*-
import codecs
from main import morph_anal
f_study = codecs.open('news_eval_train.xml', 'r', 'utf8')
f_test = codecs.open('news_eval_test.xml', 'r', 'utf8')
f_result = open('MSIP-10(result).txt', 'w')


### булевские вектора




### частоты




### tf.idf





f_study.close()
f_test.close()
f_result.close()



        f_input = open('MSIP-2(text).txt', 'w')
        f_input.write(' '.join(doc[1:]))
        f_input.close()
        morph_anal()
        f_output = codecs.open('MSIP-2(result).txt', 'r', 'utf8')


