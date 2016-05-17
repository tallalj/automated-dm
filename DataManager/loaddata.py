# -*- coding: utf-8 -*-
"""
Created on Sat May 14 01:22:26 2016

@author: taila
"""

# -*- coding: utf-8 -*-

import random
import sys
import os
import numpy as np
import scipy as sc
import matplotlib.pyplot as plt
import pandas as pd

class loaddata:
    def __init__(self):
        print("class initialized");
        
    def printingHellow(self):
        "heasdfsdf"

    file_path = "D:\\AAA  Studies\\Semester II\\DATA MINING\\Datasets\\output.json"
    data_frame=""

    def read_file_at_path(self,path):
        filename, file_extension = os.path.splitext(path)
        print(filename + " " + file_extension)
        if file_extension == ".csv":
            return self.read_csv_or_text(path)
        if file_extension == ".xls":
            return self.reading_excel_xls(path)
        return

    def read_csv_or_text(self,path):
        self.data_frame = pd.read_csv(path) #reading  csv data
        return self.data_frame #return data frame of csv file
        
    def reading_excel_xls(self,path):
        import xlrd
        workbook = xlrd.open_workbook(path)
        worksheet = workbook.sheet_by_name('titanic3')   #hardcoded
        #a = worksheet.cell(2,9).value value for specifi field
        data = [[worksheet.cell_value(r,c) for c in range (worksheet.ncols)] for r in range(worksheet.nrows)]
        data = pd.DataFrame(data)        
        return data
        
    def reading_json(self):
        #import urllib2
        import json
        with open(self.file_path) as json_data:
            data = json_data.read()
            jdata = json.loads(data)
        #jdata = pd.DataFrame(jdata)
        # print(jdata)
        return jdata

    def read_clipboard(self):
        clip_data = pd.read_clipboard()
        return clip_data

    def read_html(self):
        #import html5lib   #'''pip install pandas pip install lxml pip install html5lib pip install BeautifulSoup4
        url = 'http://www.fdic.gov/bank/individual/failed/banklist.html'
        data = pd.read_html(url)
        print(data)