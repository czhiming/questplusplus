#-*- coding:utf8 -*-
'''
Created on Sep 29, 2016

@author: czm
'''
class Processlex:
    
    fileName = ''
    word_dict = {}
    
    def __init__(self,fileName):
        self.fileName = fileName
        
    def getDict(self):
        with open(self.fileName) as fp:
            for lines in fp:
                lines = lines.strip()
                word_list = lines.split(' ')
                if word_list[0] not in self.word_dict:
                    self.word_dict[word_list[0]] = {}
                self.word_dict[word_list[0]][word_list[1]] = word_list[2]
        return self.word_dict

if __name__ == '__main__':
    pl = Processlex('/home/czm/workspace/questpy/resources/giza/lex.e2s')
    word_dict = pl.getDict()
    print len(word_dict)
    print word_dict['decentralizing']