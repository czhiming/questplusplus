#-*- coding:utf8 -*-
'''
Created on Sep 24, 2016

@author: czm
'''
class Feature1006:
    
    def __init__(self):
        pass
    
    def run(self,srcLine):
        word_list = srcLine.split(' ')
        count = []
        for word in word_list:
            count.append(len(word))
        return float(sum(count))/len(word_list)
    
    
if __name__ == '__main__':
    pass