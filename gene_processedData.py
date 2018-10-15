# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 22:28:39 2018

@author: by xubing
e-mai:xubing@613.foxmail.com
I am so young, and my story hasn't become a legend!
"""
'''
目标1：将train和valid合并形成1.all_data.csv
目标2：数据预处理，空格，保留！，。？等常见的标点，生成2.processedAllData.csv
目标3：生成-2和2的2二分类数据.3.binary_classes.csv
    目标3.5:分割数据，分割成train_set,valid_set,test_set.按照9：0.5：0.5划分。生成3.2train_set.csv,3.2valid_set.csv,3.2test_set.csv
目标4：生成-1，0，1三分类的数据。4.triple_classes.csv
    目标4.5：分割数据，分割成train_set,valid_set,test_set.按照9：0.5：0.5划分。生成4.3train_set.csv,4.3valid_set.csv,4.3test_set.csv

'''
base_dir = 'F:\\NLP\\challengerAI\\data\\sentiment_analysis\\'
import pandas as pd
strain = pd.read_csv(base_dir+'train.csv',header = 0)
svalid = pd.read_csv(base_dir+'valid.csv',header = 0)
stesta = pd.read_csv(base_dir+'testa.csv',header = 0)

###目标1
def mergeData(df1,df2):
    return pd.concat([df1,df2],axis = 'rows')
all_data = mergeData(strain,svalid)
all_data.to_csv(base_dir+'1.all_data.csv',index = False)
    
###目标2
def contentProcess(df):
    #去除空格标点符号
    #查看数据后发现content列需要处理
    '''去除空行、标点符号、数字等'''
#    from string import punctuation
#    punc = punctuation + u'.,;《》“”‘’@#￥%…&×（）——+【】{};；●&～、？。，|\s:：‘'
    punc = '.,;《》“”‘’@#￥%…&×（）——+【】{};；●&～、？。，|\s:：‘'
    import re
    content = []
    for i in range(len(df)):
        content.append(re.sub(r"[{}]+".format(punc),"",df['content'][i]))
    df['content'] = pd.Series(content)
    return df
processedAllData = contentProcess(all_data)
processedAllData = processedAllData.to_csv(base_dir + '2.processedAllData.csv',index = False)



import copy
strain = contentProcess(strain)
temp_strain = copy.deepcopy(strain)

svalid = contentProcess(svalid)     
temp_svalid = copy.deepcopy(svalid)

#strain.to_csv('binary_train.csv',sep = '\t',index = False)

#b_train,b_valid都是二分类的数据
#strain_replacedCols = strain[strain.columns[2:]].replace([-1,0,1],[2,2,2])#替换后的20列
#strain[strain.columns[2:]] = strain_replacedCols
#b_train = strain

svalid_replacedCols = svalid[svalid.columns[2:]].replace([-1,0,1],[2,2,2])
svalid[svalid.columns[2:]] = svalid_replacedCols
b_valid = svalid

#t_train,t_valid都是三分类的数据
#strain_filtedCols = temp_strain[temp_strain[temp_strain.columns[-1]] > 0 ]
#strain_filtedCols

svalid_filtedCols = temp_svalid[temp_svalid[temp_svalid.columns[2:]] > -2 ]
svalid_filtedCols.to_csv('triple_classes.csv',index = False)

#dtrain.to_csv('binaryTrain.csv',index = False)
#dvalid.to_csv('binaryValid.csv',index = False)





