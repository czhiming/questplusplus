#-*- coding:utf8 -*-
'''
Created on Sep 24, 2016

@author: czm
'''
import os

class Tokenizer:
    
    fileName = ''  #文件名
    filePath = ''  #文件路径
    shortTag = 'en' #语言，短标记
    tokenizer_path = ''
    
    def __init__(self,fileName,filePath,shortTag,tokenizer_path):
        self.fileName = fileName
        self.filePath = filePath
        self.shortTag = shortTag
        self.tokenizer_path = tokenizer_path
        
    def tokenizer(self):
        """
        执行tokenzier
        """
        #定义传入的参数
        dir_name = self.filePath.split('/')[0]
        input_name = dir_name+'/'+self.fileName
        output_name = self.filePath+'/'+self.fileName+'.tok'
        
        if os.path.exists(output_name):
            print output_name+' is already exists. Tokenizer will not run'
            return
        
        print 'running tokenizer: '+self.fileName+' to '+self.fileName+'.tok'
        sys_cmd = self.tokenizer_path+' -l '+self.shortTag+' < '+input_name+' > '+output_name
        state = os.system(sys_cmd)
        if state == 0:
            print 'SUCCESS tokenizer...'
        else:
            print 'FAILD tokenizer...'

if __name__ == '__main__':
    tk = Tokenizer('')
    tk.tokenizer()
    
    