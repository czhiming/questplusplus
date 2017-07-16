#-*- coding:utf8 -*-
'''
Created on Sep 24, 2016

@author: czm
'''
from shef.mt.features.util.Sentence import Sentence

class Feature1015:
    
    def __init__(self):
        pass
    
    def run(self,tgtLine):
        st = Sentence(tgtLine)
        count = st.get_punc_num()
        
        word_list = tgtLine.split(' ')
        word_set = set(word_list)
        word_set = map(lambda x:x.lower(),word_set)
        
        return float(len(word_list))/(len(word_set)-count)

if __name__ == '__main__':
    ft = Feature1015()
    result = ft.run('/home/czm/workspace/questpy/resources/giza/lex.e2s', '/home/czm/workspace/questpy/input/target.es')
    print result
    
    
    
    