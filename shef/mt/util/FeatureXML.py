#-*- coding:utf8 -*-
'''
Created on Sep 24, 2016

@author: czm
'''
'''
处理xml特征文件，获取每个特征所对应的类
'''
import xml.dom.minidom


class FeatureXML:
    
    xmlFile = ''
    xmlFeature = {}
    
    def __init__(self,xmlFile):
        self.xmlFile = xmlFile
    
    def getxmlFeature(self):
        """
        获取xmlFile文件中的内容
        """
        dom = xml.dom.minidom.parse(self.xmlFile)
        root = dom.documentElement
        features = root.getElementsByTagName('feature')
        for feature in features:
            index =  feature.getAttribute('index').encode('utf8')
            description = feature.getAttribute('description').encode('utf8')
            class_name = feature.getAttribute('class').encode('utf8')
            self.xmlFeature[index] = class_name,description
        return self.xmlFeature



if __name__ == '__main__':
    fx = FeatureXML('/home/czm/workspace/questpy/config/features/features_blackbox_17.xml')
    print fx.getxmlFeature()
    
    
    
    
    