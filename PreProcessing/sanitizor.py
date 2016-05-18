import pandas as pd
import numpy as np
from scipy import stats


class sanitizor:
    "Documentation string"
    test = 0

    def __init__(self):
        "nothing usefull here"

    def displayClass(self):
        print("class is sanitizor")

    def removeOutliers(self):
        print("removes the outliers from the set data frame")

    def replaceMissingWithMeans(self):
        "replaces all the missing values with the mean values"
        print("replacing missing data with means")

    


    #Mubashir
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
        m = 1.5
        u = np.mean(data)
        s = np.std(data)
        filtered = [e for e in data if (u - 1.5 * s < e < u + 1.5 * s)]
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
        c = np.cov(d, rowvar=False)
        return c

    def get_var(d):
        c = np.var(d)
        return c
        
        
    def count_outliers(col):
        old = col
        new = col
        if col.dtype != np.float32 and col.dtype != np.float64 and col.dtype != np.int64:
            return 0
        else:
            new = reject_outliers1(col)
            return len(old)-len(new)
            


    print(count_outliers(df.ix[:,9]))        
            

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



    #Analyze complete df
    def analyze_df(df):
        desc = df.describe()
        info = df.info()
        d = remove_non_numeric(df)
        m = remove_nan_by_mean(d)
        co = get_cov(m)
        va = get_var(m)
        nan = count_nan_col_total(df)
        return("\n\nSummary statistics\n"+str(desc)+
        "\n\nInfo\n"+str(info)+
        "\n\nCovarience Matrix\n"+str(co)+
        "\n\nVarience Matrix\n"+str(va)+
        "\n\nTotal Missing Values in dataframe\n"+str(nan)+"\n"
        )
        #print(info)
        #print(co)
        #print(va)

    
    #Analyze single col    
    def analyze_col(col):
        des = col.describe()
        out = count_outliers(col)
        return("\n\nSummary statistics\n"+str(des)+
        "\n\nOutliers\n"+str(out))
        
