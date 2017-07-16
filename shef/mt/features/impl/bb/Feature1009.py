#-*- coding:utf8 -*-
'''
Created on Sep 24, 2016

@author: czm
'''
from shef.mt.features.util.Processppl import Processppl

class Feature1009:

        
    def run(self,srcFile,srcDir):
        pc = Processppl(srcFile,srcDir)
        result = pc.processppl()
        return result
    
if __name__ == '__main__':
    pass