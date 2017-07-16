#-*- coding:utf8 -*-
'''
Created on Sep 24, 2016

@author: czm
'''
class Feature1049:
    
    def __init__(self):
        pass
    
    def run(self,srcLine,unigram_freq):
        word_freq = unigram_freq
        word_sort = sorted(word_freq.iteritems(),key=lambda x:x[1])
        word_src = srcLine.split(' ')
        
        flag1 = len(word_sort)/4
        flag3 = len(word_sort)*3/4
        
        count = 0
        for word in word_src:
            if word in word_freq:
                for i,w in enumerate(word_sort):
                    if w[0] == word:
                        if i >= flag3:
                            count += 1
        return float(count)/len(word_src)
if __name__ == '__main__':
    pass