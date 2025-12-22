#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 19:47:08 2023

@author: sidhant
"""
import pandas as pd
import numpy as np

#------------ Trial
#By ChatGPT
data = {
    'Column1': [1, 2, np.nan, np.nan, 5, 6, 7, np.nan, 9, 10],
    'Column2': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I','L']
}
df=pd.DataFrame(data)
def remove_na_and_above_final(df):
    na_mask = df['Column1'].isna()
    # Shift the NaN mask, filling the last value with False instead of NaN
    prev_na_mask = na_mask.shift(-1).fillna(False) & (~na_mask)
    combined_mask = na_mask | prev_na_mask
    return df[~combined_mask]
#-------------------

#my code
def remove_na_above(df):
    nas=df.iloc[:,0].isna()#find na in first column only
    x=[i for i in range(len(nas)) if nas[i]==True]
    a=[i-1 for i in x]
    m=list(set(x+a))#to remove NA row and row above it
    df=df.drop(m)
    return df


data1=pd.read_csv('all',sep=',')
print(data1)
data1=remove_na_above(data1)#remove multimers
data1=data1.dropna()# drop other entries which doesn't have uniprot id
#data1.to_csv('all_filtered',sep='\t',index=False)#writing file.
