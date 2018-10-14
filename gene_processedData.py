# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 22:28:39 2018

@author: by xubing
e-mai:xubing@613.foxmail.com
I am so young, and my story hasn't become a legend!
"""
'''
目标1：数据预处理
目标2：生成-2和2的2分类数据。生成-1，0，1三分类的数据。
'''
base_dir = 'F:\\NLP\\challenger.ai\\sentiment_analysis\\data\\data\\'
import pandas as pd
strain = pd.read_csv(base_dir+'train.csv',header = 0)
svalid = pd.read_csv(base_dir+'valid.csv',header = 0)
stesta = pd.read_csv(base_dir+'testa.csv',header = 0)
#pd.set_option('display.max_colwidth',500)
#print(strain.head())
#print(strain.tail())

def contentProcess(content):
    #去除空格标点符号
    #
    

strain_replacedCols = strain[strain.columns[2:]].replace([-1,0,1],[2,2,2])#替换后的20列
strain[strain.columns[2:]] = strain_replacedCols
strain_replacedData = strain


