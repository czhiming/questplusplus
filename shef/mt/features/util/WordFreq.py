#-*- coding:utf8 -*-
'''
Created on Sep 29, 2016

@author: czm
'''
from shef.mt.features.util.Sentence import Sentence
class WordFreq:
    source_corpus = ''
    
    def __init__(self,source_corpus):
        self.source_corpus = source_corpus
    
    def get_unigram_Freq(self):
        word_freq = {}
        for lines in open(self.source_corpus):
            lines = lines.strip()
            word_list = lines.split(' ')
            for word in word_list:
                if word not in word_freq:
                    word_freq[word] = 0
                word_freq[word] += 1
        return word_freq
    
    def get_bigram_Freq(self):
        word_freq = {}
        for lines in open(self.source_corpus):
            lines = lines.strip()
            st = Sentence(lines)
            lines = st.get_bigram()
            word_list = lines.split(' ')
            for word in word_list:
                if word not in word_freq:
                    word_freq[word] = 0
                word_freq[word] += 1
        return word_freq
    
    def get_trigram_Freq(self):
        word_freq = {}
        for lines in open(self.source_corpus):
            lines = lines.strip()
            st = Sentence(lines)
            lines = st.get_trigram()
            word_list = lines.split(' ')
            for word in word_list:
                if word not in word_freq:
                    word_freq[word] = 0
                word_freq[word] += 1
        return word_freq
    
    









if __name__ == '__main__':
    pass