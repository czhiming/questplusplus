#-*- coding:utf8 -*-
'''
Created on Sep 24, 2016

@author: czm
'''
import re
from shef.mt.features.util.Sentence import Sentence

class Feature1074:
    
    def __init__(self):
        pass
    
    def run(self,srcLines):
        st = Sentence(srcLines)
        count = st.get_punc_num()
        return float(count)

if __name__ == '__main__':
    ft = Feature1074()
    print ft.run("mr. englund is a swedish historian and journalist . ")