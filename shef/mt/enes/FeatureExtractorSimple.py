#-*- coding:utf8 -*-
'''
Created on Sep 24, 2016

@author: czm
'''
from shef.mt.util.GetConfig import GetConfig
from shef.mt.util.FeatureXML import FeatureXML
from shef.mt.util.Tokenizer import Tokenizer
from shef.mt.util.Truecase import Truecase
from shef.mt.util.MakePerplexity import MakePerplexity
from shef.mt.features.util.Processlex import Processlex
from shef.mt.features.util.WordFreq import WordFreq
from shef.mt.features.util.Sentence import Sentence

import importlib
import os

class FeatureExtractorSimple:
    
    #存储配置文件的内容
    config = {}
    #存储要提取的特征类型，bb/gb
    mode = ''
    #存储xml文件中要提取的特征
    xmlFeature = {}
    #排序后的特征索引列表
    index_list = []  
    
    
    
    def __init__(self,configFile):
        """
        获取配置文件的内容
        """
        gc = GetConfig(configFile)  #配置文件在命令行传入
        self.config = gc.getConfig()
        self.input_dir = self.config['input']
        self.output_dir = self.config['output']
        self.source_file = self.config['src.file'].split('/')[1]
        self.target_file = self.config['tgt.file'].split('/')[1]
        self.source_dir = self.config['sourceLang.default']
        self.target_dir = self.config['targetLang.default']
        self.source_tag = self.getShortTag(self.config['sourceLang.default'])
        self.target_tag = self.getShortTag(self.config['targetLang.default'])
        self.source_tok = self.config['src.tokenizer']
        self.target_tok = self.config['tgt.tokenizer']
        self.source_true = self.config['src.truecase']
        self.target_true = self.config['tgt.truecase']
        self.source_true_model = self.config['src.truecase.model']
        self.target_true_model = self.config['tgt.truecase.model']
        self.source_ngram_path = self.config['src.ngramscript.path']
        self.target_ngram_path = self.config['tgt.ngramscript.path']
        self.giza_path = self.config['giza.path']
        self.source_corpus = self.config['src.corpus']
    
    def getxmlFeature(self):
        """
        获取xml文件的内容
        """
        fx = FeatureXML(self.config['featureConfig.bb'])
        self.xmlFeature = fx.getxmlFeature()
        self.index_list = sorted(self.xmlFeature)
        
    def getShortTag(self,language):
        """
        获取语言的短标记
        """
        if language.lower() == 'english':
            return 'en'
        elif language.lower() == 'spanish':
            return 'es'
        elif language.lower() == 'french':
            return 'fr'
        elif language.lower() == 'german':
            return 'de'
        elif language.lower() == 'dutch':
            return 'nl'
        elif language.lower() == 'portuguese':
            return 'pt'
        else:
            return "Don't recognise the source language"
            
    def createDirectory(self):
        """
        在input目录中，创建对应的目录
        """
        print 'createDirectory...'
        
        if os.path.exists(self.input_dir+'/'+self.source_dir) == False:
            os.mkdir(self.input_dir+'/'+self.source_dir)
        if os.path.exists(self.input_dir+'/'+self.target_dir) == False:
            os.mkdir(self.input_dir+'/'+self.target_dir)
        
    def preprocessing(self):
        #获取config中的各种值
        
        
        #tokenizer 源语言和目标语言
        tk = Tokenizer(self.source_file,self.input_dir+'/'+self.source_dir,self.source_tag,self.source_tok)
        tk.tokenizer()
        tk = Tokenizer(self.target_file,self.input_dir+'/'+self.target_dir,self.target_tag,self.target_tok)
        tk.tokenizer()
        
        #truecase 源语言和目标语言
        '''
        tc = Truecase(source_file,input_dir+'/'+source_dir,source_true,source_true_model)
        tc.truecase()
        tc = Truecase(target_file,input_dir+'/'+target_dir,target_true,target_true_model)
        tc.truecase()
        '''
        
        #借助 SRILM 生成源语言句子和目标语言句子的，对数概率和困惑度
        mp = MakePerplexity(self.source_file,self.input_dir+'/'+self.source_dir,self.config['src.lm'],self.source_ngram_path)
        mp.makeppl()
        mp = MakePerplexity(self.target_file,self.input_dir+'/'+self.target_dir,self.config['tgt.lm'],self.target_ngram_path)
        mp.makeppl()
        
        
    def prepare(self):
        """
        运行之前的准备
        """
        #self.getConfig()  #获取配置文件
        self.getxmlFeature() #获取特征
        self.createDirectory() #创建相应目录
        self.preprocessing() #语料预处理，生成需要的各种文件

        
    def runBB(self):
        #准备阶段
        self.prepare()
        #获得源语言，和目标语言句子
        source = []
        target = []
        for lines in open(self.input_dir+'/'+self.source_dir+'/'+self.source_file+'.tok'):
            lines = lines.strip()
            source.append(lines)
        for lines in open(self.input_dir+'/'+self.target_dir+'/'+self.target_file+'.tok'):
            lines = lines.strip()
            target.append(lines)
        
        #返回的特征向量
        features = []
        print '********* processing Features *********'

        #实现各特征前的准备阶段
        #lex.e2s, Feature1022,
        pl = Processlex(self.giza_path)
        lex_dict = pl.getDict()
        #Feature 1036
        wf = WordFreq(self.source_corpus)
        unigram_freq = wf.get_unigram_Freq()
        bigram_freq = wf.get_bigram_Freq()
        trigram_freq = wf.get_trigram_Freq()

        for i,lines in enumerate(source): 
            feature_vec = []
            
            print 'processing line number '+str(i)+' ...'
            
            for index in self.index_list:
                class_name = self.xmlFeature[index][0]
                module_name = 'Feature'+index
                module = importlib.import_module(class_name)
                ####
                # 从此处开始，添加各种特征
                ####
                #Feature1001, number of tokens in the source sentence
                if index == '1001':
                    print '----------1001----------'
                    module_name = getattr(module,module_name)
                    ft = module_name()
                    num = ft.run(lines)
                    feature_vec.append(float(num))
                #Feature1002, number of tokens in the target sentence
                if index == '1002':
                    print '----------1002----------'
                    module_name = getattr(module,module_name)
                    ft = module_name()
                    num = ft.run(target[i])
                    feature_vec.append(float(num))
                #Feature1006, average source token length
                if index == '1006':
                    print '----------1006----------'
                    module_name = getattr(module,module_name)
                    ft = module_name()
                    num = ft.run(lines)
                    feature_vec.append(float(num))
                #Feature1009, LM log probability of source sentence
                if index == '1009':
                    print '----------1009----------'
                    module_name = getattr(module,module_name)
                    ft = module_name()
                    result = ft.run(self.source_file,self.input_dir+'/'+self.source_dir+'/')
                    feature_vec.append(float(result[i][0]))
                #Feature 1012, LM log probability of target sentence
                if index == '1012':
                    print '----------1012----------'
                    module_name = getattr(module,module_name)
                    ft = module_name()
                    result = ft.run(self.target_file,self.input_dir+'/'+self.target_dir+'/')
                    feature_vec.append(float(result[i][0]))
                #Feature 1015, number of occurences of the target word with the target hypothesis
                if index == '1015':
                    print '----------1015----------'
                    module_name = getattr(module,module_name)
                    ft = module_name()
                    result = ft.run(target[i])
                    feature_vec.append(result)
                #Feature 1022, average number of transaltions per source word in the sentence
                if index == '1022':
                    print '----------1022----------'
                    module_name = getattr(module,module_name)
                    ft = module_name()
                    result = ft.run(lex_dict,lines)
                    feature_vec.append(result)
                #Feature 1036
                if index == '1036':
                    print '----------1036----------'
                    module_name = getattr(module,module_name)
                    ft = module_name()
                    result = ft.run(lex_dict,lines,unigram_freq)
                    feature_vec.append(result)
                #Feature 1046
                if index == '1046':
                    print '----------1046----------'
                    module_name = getattr(module,module_name)
                    ft = module_name()
                    result = ft.run(lines,unigram_freq)
                    feature_vec.append(result)
                #Feature 1049
                if index == '1049':
                    print '----------1049----------'
                    module_name = getattr(module,module_name)
                    ft = module_name()
                    result = ft.run(lines,unigram_freq)
                    feature_vec.append(result)
                if index == '1050':
                    print '----------1050----------'
                    module_name = getattr(module,module_name)
                    ft = module_name()
                    result = ft.run(lines,bigram_freq)
                    feature_vec.append(result)
                if index == '1053':
                    print '----------1053----------'
                    module_name = getattr(module,module_name)
                    ft = module_name()
                    result = ft.run(lines,bigram_freq)
                    feature_vec.append(result)
                if index == '1054':
                    print '----------1054----------'
                    module_name = getattr(module,module_name)
                    ft = module_name()
                    result = ft.run(lines,trigram_freq)
                    feature_vec.append(result)
                if index == '1057':
                    print '----------1057----------'
                    module_name = getattr(module,module_name)
                    ft = module_name()
                    result = ft.run(lines,trigram_freq)
                    feature_vec.append(result)
                if index == '1058':
                    print '----------1058----------'
                    module_name = getattr(module,module_name)
                    ft = module_name()
                    result = ft.run(lines,unigram_freq)
                    feature_vec.append(result)
                #Feature 1074, number of punctuation marks in the source sentence
                if index == '1074':
                    print '----------1074----------'
                    module_name = getattr(module,module_name)
                    ft = module_name()
                    result = ft.run(lines)
                    feature_vec.append(result)
                #Feature 1075, number of punctuation marks in the target sentence
                if index == '1075':
                    print '----------1075----------'
                    module_name = getattr(module,module_name)
                    ft = module_name()
                    result = ft.run(target[i])
                    feature_vec.append(result)
                
                
            features.append(feature_vec)
            
        return features

       
            



if __name__ == '__main__':
    pass