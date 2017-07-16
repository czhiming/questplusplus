#-*- coding:utf8 -*-
'''
Created on Sep 24, 2016

@author: czm
'''
import re
from shef.mt.features.util.Sentence import Sentence

class Feature1075:
    
    def __init__(self):
        pass
    
    def run(self,tgtLine):
        st = Sentence(tgtLine)
        count = st.get_punc_num()
        return float(count)


if __name__ == '__main__':
    pass