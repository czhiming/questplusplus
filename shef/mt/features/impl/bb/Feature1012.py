#-*- coding:utf8 -*-
'''
Created on Sep 24, 2016

@author: czm
'''
from shef.mt.features.util.Processppl import Processppl

class Feature1012:

        
    def run(self,tgtFile,tgtDir):
        pc = Processppl(tgtFile,tgtDir)
        result = pc.processppl()
        return result
    
if __name__ == '__main__':
    pass