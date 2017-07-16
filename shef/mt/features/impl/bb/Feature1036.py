#-*- coding:utf8 -*-
'''
Created on Sep 24, 2016

@author: czm
'''
from shef.mt.features.util.Processlex import Processlex

from collections import Counter
import numpy as np

class Feature1036:
    
    def __init__(self):
        pass
    
    def run(self,lex_dict,srcLine,word_freq):

        word_list = srcLine.split(' ')
        ct = Counter(word_list)
        
        word_dict = lex_dict
        count = [0]*len(word_list)
        
        word_idf = [0]*len(word_list)
        for i,word in enumerate(word_list):
            if word in word_freq:
                word_idf[i] = word_freq[word]
        
        
        idf_vec = [0]*len(word_list)
        for i,word in enumerate(word_list):
            idf_vec[i] = float(ct[word])/(word_idf[i]+1)
        
        for i,key in enumerate(word_list):
            if key in word_dict:
                for key_id in word_dict[key]:
                    if float(word_dict[key][key_id]) > 0.01:
                        count[i] += 1
 
        count = np.array(count,dtype=float)
        idf_vec = np.array(idf_vec,dtype=float)
        
        return sum(idf_vec*count)/len(word_list)
        

if __name__ == '__main__':
    ft = Feature1036()
    ft.run('','','')
    