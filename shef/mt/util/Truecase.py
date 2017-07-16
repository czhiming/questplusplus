#-*- coding:utf8 -*-
'''
Created on Sep 24, 2016

@author: czm
'''
import os

class Truecase:
    
    fileName = ''
    filePath = ''
    truecase_path = ''
    truecase_model = ''
    
    def __init__(self,fileName,filePath,truecase_path,truecase_model):
        self.fileName = fileName
        self.filePath = filePath
        self.truecase_path = truecase_path
        self.truecase_model = truecase_model
        
    def truecase(self):
        """
        执行truecase操作
        """
        #定义传入的参数
        file_tok = self.fileName+'.tok'  #上一步生成的文件名
        input_name = self.filePath+'/'+file_tok
        output_name = self.filePath+'/'+self.fileName+'.true'
        
        if os.path.exists(output_name):
            print output_name+' is already exists. Truecase will not run'
            return 
        
        print 'running truecase: '+file_tok+' to '+self.fileName+'.true'
        state = os.system(self.truecase_path+' --model '+self.truecase_model+' < '+input_name+' > '+output_name)
        if state == 0:
            print 'SUCCESS truecase...'
        else:
            print 'FAILD truecase...'





if __name__ == '__main__':
    
    
    
    
    pass