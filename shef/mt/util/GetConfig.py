#-*- coding:utf8 -*-
'''
Created on Sep 24, 2016

@author: czm
'''
import re

class GetConfig:
    
    config = {}
    pattern = re.compile(r'!.*')
    
    def __init__(self,configFile):
        with open(configFile) as cf:
            for lines in cf:
                lines = lines.strip()
                #lines is null
                if lines == '':
                    pass
                elif self.pattern.match(lines) != None:
                    pass
                else:
                    kv = re.split(r'[ =]+',lines)
                    key = kv[0]
                    value = kv[1]
                    self.config[key] = value
    def getConfig(self):
        return self.config



if __name__ == '__main__':
    gc = GetConfig('/home/czm/workspace/questpy/config/config_en-es.properties')
    config = gc.getConfig()
    print config