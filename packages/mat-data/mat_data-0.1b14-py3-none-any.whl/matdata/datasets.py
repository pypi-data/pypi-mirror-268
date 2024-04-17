# -*- coding: utf-8 -*-
"""
Multiple Aspect Trajectory Tools Framework, MAT-data: Data Preprocessing for Multiple Aspect Trajectory Data Mining

The present application offers a tool, to support the user in the classification task of multiple aspect trajectories,
specifically for extracting and visualizing the movelets, the parts of the trajectory that better discriminate a class.
It integrates into a unique platform the fragmented approaches available for multiple aspects trajectories and in
general for multidimensional sequence classification into a unique web-based and python library system. Offers both
movelets visualization and classification methods.

Created on Dec, 2023
Copyright (C) 2023, License GPL Version 3 or superior (see LICENSE file)

@author: Tarlis Portela
"""
import os
import pandas as pd
import numpy as np

from tqdm.auto import tqdm

from matdata.preprocess import organizeFrame, splitTIDs, readDataset

BASE_URL = 'https://raw.githubusercontent.com/bigdata-ufsc/datasets_v1_0/main/data/'

DATASET_TYPES = {
    'mat':                       'Multiple Aspect Trajectories', 
    'raw':                       'Raw Trajectories', 
    'sequential':                'Sequential Semantics', 
    'process':                   'Event Logs',
    'multivariate_ts':           'Multivariate Time Series', 
    'univariate_ts':             'Univariate Time Series',
}

SUBSET_TYPES = {
   '*.specific':                     'Multiple',
   'mat.specific':                   'Multiple Aspect',
   'raw.specific':                   'Raw',
   'sequential.*':                   'Semantic',
   'multivariate_ts.specific':       'Multivariate',
   'univariate_ts.specific':         'Univariate',
#    'process.specific':               'Event Log',
   'process.process':                'Event Log',
   'process.*':                      'Semantic',
    
   '*.raw':      'Spatio-Temporal',
    
   '*.spatial':  'Spatial',
   '*.geo_only': 'Spatial',
   '*.generic':  'Generic',
   '*.category': 'Category',
   '*.poi':      'POI',
   '*.5dims':    '5-Dimensions',
   '*.genes':    'Genetic Sequence',
}

###############################################################################
#   LOAD DATASETs - From https://github.com/bigdata-ufsc/datasets_v1_0
###############################################################################
def prepare_ds(df, sample_size=1, random_num=1):
    df.sort_values(['tid', 'label'])
    
    if sample_size < 1: # Stratify the data
        df_index, _, _ = splitTIDs(df, sample_size, random_num, 'tid', 'label', min_elements=2)

        df = df.loc[df['tid'].isin(df_index)]
        
    df, columns_order_zip, columns_order_csv = organizeFrame(df, None, 'tid', 'label')
        
    return df[columns_order_csv]

def read_ds(data_file, tid_col='tid', class_col='label', missing='-999', sample_size=1, random_num=1):
    df = readDataset(data_file, class_col='label', missing=missing)
    
    df.rename(columns={tid_col: 'tid', class_col: 'label'}, inplace=True)
    
    return prepare_ds(df, sample_size, random_num)

def load_ds(dataset='mat.FoursquareNYC', prefix='specific', missing='-999', sample_size=1, random_num=1):
    
    df = load_ds_holdout(dataset, prefix, missing)
    
    df = pd.concat(df)
    
    return prepare_ds(df, sample_size, random_num)

def load_ds_5fold(dataset='mat.FoursquareNYC', prefix='specific', missing='-999'):
    
    dsc = dataset.split('.')[0]
    dsn = dataset.split('.')[1]
    
    k_train = []
    k_test  = []
    
    for fold in tqdm(range(1, 6), desc='Reading 5-fold dataset '+ dsn + ' of ' + translateCategory(dsn, dsc)):
        df_train, df_test = load_ds_holdout(dataset, prefix, missing, fold)
        
        k_train.append(df_train)
        k_test.append(df_test)
        
    return k_train, k_test

def load_ds_holdout(dataset='mat.FoursquareNYC', prefix='specific', missing='-999', fold=None):
    
    dsc = dataset.split('.')[0]
    dsn = dataset.split('.')[1]

    if prefix and prefix != '':
        files = [prefix+'_train.csv', prefix+'_test.csv']
    else:
        files = ['train.csv', 'test.csv']
        
    if fold:
        files = ['run'+str(fold)+'/'+files[0], 'run'+str(fold)+'/'+files[1]]
    else:
        print('Reading dataset', dsn, 'of', translateCategory(dsn, dsc))
    
    dataset = []
    for file in tqdm(files, desc=dsn + ' (' + translateCategory(dsn, dsc) + \
                     ('), fold: '+str(fold) if fold else ')')):
        url = BASE_URL + dsc+'/'+dsn+'/' + file
        df = pd.read_csv(url) #, na_values=missing)
        df.fillna(missing, inplace=True)
        dataset.append(df)
    
    return dataset
    
# ------------------------------------------------------------
def translateDesc(dataset, category, descName):
    dst, dsn = descName.split('.')[0].split('_')[0:2]
    if dsn in ['allfeat', '5dims']:
        return False

    if getDescName(category, dataset) == dst:
        return dsn
    elif dataset in dst:
        return dsn
    return False

def translateCategory(dataset, category, descName=None):
    if descName:        
        if (category+'.'+descName) in SUBSET_TYPES.keys():
            return SUBSET_TYPES[category+'.'+descName]
        elif ('*.'+descName) in SUBSET_TYPES.keys():
            return SUBSET_TYPES['*.'+descName]
        elif (category+'.*') in SUBSET_TYPES.keys():
            return SUBSET_TYPES[category+'.*']
        else:
            return descName.capitalize()
        
    elif category in DATASET_TYPES.keys():
        return DATASET_TYPES[category]
    
    else:
        return category.split('_')[0].title()
    
# ------------------------------------------------------------
#def getName(dic, dst=None, dsn=None):
#    dst = (dst if dst else '*')
#    dsn = (dsn if dsn else '*')
#    if dst +'.'+ dsn in dic.keys():
#        name = dic[dst +'.'+ dsn]
#    elif dst +'.*' in dic.keys():
#        name = dic[dst +'.*']
#    elif '*.*' in dic.keys():
#        name = dic['*.*']
#        
#    if not name:
#        name = dsn 
#    return name
#
#def getDescName(dst, dsn):
#    name = getName(DESCRIPTOR_NAMES, dst, dsn)
#    if not name:
#        name = dsn
#    return name
#
#def getFeature(dst, dsn):
#    name = getName(FEATURES_NAMES, dst, dsn)
#    if not name:
#        name = ['poi']
#    return name
#
#def getSubset(dsn, feature):
#    for key, value in FEATURES_NAMES.items():
#        if dsn in key and feature in value:
#            if '?' in key:
#                return 'generic'
#            
#    return 'specific'