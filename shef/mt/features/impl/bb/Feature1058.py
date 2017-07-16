#-*- coding:utf8 -*-
'''
Created on Sep 24, 2016

@author: czm
'''
class Feature1058:
    
    def __init__(self):
        pass
    
    def run(self,srcLine,unigram_freq):
        word_dict = unigram_freq

        word_src = srcLine.split(' ')
        
        count = 0
        for word in word_src:
            if word in word_dict:
                count += 1
        return float(count)/len(word_src)
if __name__ == '__main__':
    pass