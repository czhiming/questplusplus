#-*- coding:utf8 -*-
'''
Created on Oct 8, 2016

@author: czm
'''
import re

class Sentence:
    
    count = 0  #标点符号的数量
    sentence = ''
    pattern = re.compile(r"[.,؟¿،؛¡!?:;']")
    
    def __init__(self,sentence):
        self.sentence = sentence
    
    def get_punc_num(self):
        """
        统计句子中标点符号的数目
        """
        
        word_list = self.sentence.split(' ')
        for word in word_list:
            if self.pattern.match(word):
                self.count += 1
        return self.count
    def get_sen_rpunc(self):
        """
        去除标点符号的句子
        """
        word_list = self.sentence.split(' ')
        word_new = []
        for word in word_list:
            if self.pattern.match(word):
                pass
            else:
                word_new.append(word)
        return ' '.join(word_new)
    def get_bigram(self):
        """
        获得句子的二元文法
        """
        word_list = self.sentence.split(' ')
        word_new = []
        for i in range(len(word_list)-1):
            word_new.append(' '.join(word_list[i:i+2]))
        return ' '.join(word_new)
    def get_trigram(self):
        """
        获得句子的三元文法
        """
        word_list = self.sentence.split(' ')
        word_new = []
        for i in range(len(word_list)-2):
            word_new.append(' '.join(word_list[i:i+3]))
        return ' '.join(word_new)
        
if __name__ == '__main__':
    pass