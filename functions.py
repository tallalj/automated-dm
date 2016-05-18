# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np
from scipy import stats



def count_nan_row(df):
   c = df.isnull().sum(axis=1)
   return c

def count_nan_row_total(df):
   c = df.isnull().sum(axis=1).sum()
   return c

def count_nan_col(df):
   c = df.isnull().sum()
   return c

def count_nan_col_total(df):
   c = df.isnull().sum().sum()
   return c
   
def get_type(col):
    return col.dtype
   

def reject_outliers(data, m = 2):
    d = np.abs(data - np.median(data))
    mdev = np.median(d)
    s = d/mdev if mdev else 0
    return data[s<m]
    

def remove_non_numeric(d):
    dt = d
    for col in d:
        if  d.ix[:,col].dtype != np.float32 and d.ix[:,col].dtype != np.float64 and d.ix[:,col].dtype != np.int64:
            #print(col)
            dt=dt.drop(col,axis=1)
            #df[df.ix[:,col].apply(lambda x: x.isnumeric())]
    return dt


def is_non_numeric(d):
    if  d.dtype != np.float32 and d.dtype != np.float64 and d.dtype != np.int64:
        return False
    else:
        return True


def reject_outliers1(data):
    m = 2
    u = np.mean(data)
    s = np.std(data)
    filtered = [e for e in data if (u - 2 * s < e < u + 2 * s)]
    return filtered
    
def remove_nan_by_mean(d_f):
    data = d_f.fillna(d_f.mean())    
    return data
    
def describe_col(col):
    return col.describe()

def info_df(d):
    return d.info()

def describe_df(d):
    return d.describe()

def get_cov(d):
    c = np.cov(data, rowvar=False)
    return c

def get_var(d):
    c = np.var(data)
    return c


#def get_mean(d):
#    m = d.mean()
#    return m

#def get_mode(d):
#    m = d.mode()
#    return m

#def get_mean(d):
#    m = d.mean()
#    return m


def get_var(d):
    c = np.var(data)
    return c




def analyze_df(df,window):
    desc = df.describe()
    info = df.info()
    d = remove_non_numeric(df)
    m = remove_nan_by_mean(d)
    co = get_cov(m)
    va = get_var(m)
    print(co.dtype)
    
    
    
    


df = pd.read_csv("t_1.csv",low_memory=False)

analyze_df(df)


print(get_mode(df))

d2 = df

print(describe_df(df))

data = remove_non_numeric(df)


print(remove_mean(data))

data = remove_non_numeric(df)

print(reject_outliers1(data.ix[1]))

print(count_nan_col_total(df))

data = df.ix[2]

d = data.fillna(data.mean())
print(count_nan_col_total(d))




#print(df)

#print(count_nan_row_total(df))

non_num = remove_non_numeric(df)

out = reject_outliers(non_num)
print(out)


#out = non_num


#o =out[(np.abs(stats.zscore(out)) < 3).all(axis=1)]

#print(o)

#o = out[out.apply(lambda x: np.abs(x - x.mean()) / x.std() < 3).all(axis=1)]
#print(o)

#print(df.ix[:,0].dtype)


#df[df[.apply(lambda x: type(x) in [int, np.int64, float, np.float64])]

#print(get_type(df.ix[:,155]))
