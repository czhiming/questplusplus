#-*- coding:utf8 -*-
'''
Created on Sep 25, 2016

@author: czm
'''
import re

class Processppl:
    
    fileName = ''
    filePath = ''
    pattern = re.compile(r'logprob= (\S*?) ppl= (\S*?) ppl1= (\S*?)$')
        
    def __init__(self,fileName,filePath):
        self.fileName = fileName
        self.filePath = filePath
    
    def processppl(self):
        result = []
        with open(self.filePath+self.fileName+'.ppl') as fp:
            for lines in fp:
                lines = lines.strip()
                res = self.pattern.findall(lines)
                if res == []:
                    pass
                else:
                    result.append(res[0])
        return result



if __name__ == '__main__':
    pc = Processppl('source.en','/home/czm/workspace/questpy/input/english/')
    pc.processppl()
    
    
    
    