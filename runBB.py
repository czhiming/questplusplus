#-*- coding:utf8 -*-
'''
Created on Sep 24, 2016

@author: czm
'''
from shef.mt.enes.FeatureExtractorSimple import FeatureExtractorSimple
import time
import sys


t = time.time()
print '*******************************'
print 'starting'
print '*******************************'

#默认的 config 文件
configFile = 'config/config_en-es.properties'

if len(sys.argv)<2:
    print 'python runBB.py config/config_en-es.properties'
    exit()
else:
    configFile = sys.argv[1]

fe = FeatureExtractorSimple(configFile)
result = fe.runBB()
with open(fe.output_dir+'/'+fe.source_file+'.tok'+'_to_'+fe.target_file+'.tok','w') as fp:
    for rows in result:
        lines = '\t'.join(map(lambda x:str(x),rows))
        fp.writelines(lines+'\n')

print '*******************************'
print 'processing completed in '+'%.2f' % (time.time()-t)+' seconds.'
print '*******************************'














if __name__ == '__main__':
    pass
