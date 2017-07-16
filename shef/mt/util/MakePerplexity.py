#-*- coding:utf8 -*-
'''
Created on Sep 25, 2016

@author: czm
'''
import os

class MakePerplexity:
    
    fileName = ''
    filePath = ''
    lmName = ''
    ngram_path = ''
    
    def __init__(self,fileName,filePath,lmName,ngram_path):
        self.fileName = fileName
        self.filePath = filePath
        self.lmName = lmName
        self.ngram_path = ngram_path
        
    def makeppl(self):
        #定义输入参数
        file_true = self.fileName+'.tok'  #上一步得出的文件名
        input_name = self.filePath+'/'+file_true
        output_name = self.filePath+'/'+self.fileName+'.ppl'
        
        if os.path.exists(output_name):
            print output_name+' is already exists. makePPL will not run'
            return
        
        print 'make ppl: '+self.fileName+'.ppl'
        sys_cmd = self.ngram_path+' -ppl '+input_name+' -order 3 -lm '+self.lmName+' -debug 2 > '+output_name
        state = os.system(sys_cmd)
        if state == 0:
            print 'SUCCESS ppl...'
        else:
            print 'FAILED ppl...'



if __name__ == '__main__':
    mp = MakePerplexity('source.en.tok.true','input/english/','resources/trainfile.en.lm')
    print mp.makeppl()
    
    
    