#-*- coding:utf8 -*-
'''
Created on Sep 24, 2016

@author: czm
'''
from shef.mt.features.util.Processlex import Processlex
from shef.mt.features.util.Sentence import Sentence

class Feature1022:
    
    def __init__(self):
        pass
    
    def run(self,lex_dict,srcLines):
        word_dict = lex_dict
        word_list = srcLines.split(' ')
        
        sum = 0
        for key in word_list:
            if key in word_dict:
                for key_id in word_dict[key]:
                    if float(word_dict[key][key_id]) > 0.2:
                        sum += 1
        
        return float(sum)/len(word_list)


if __name__ == '__main__':
    ft = Feature1022()
    result = ft.run('/home/czm/workspace/questpy/resources/giza/lex.e2s', '/home/czm/workspace/questpy/input/source.en')
    print result
    
    