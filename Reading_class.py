# -*- coding: utf-8 -*-
"""
Created on Sat May 14 01:22:26 2016

@author: taila
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random
import sys
import os
import numpy as np
import scipy as sc
import matplotlib.pyplot as plt
import pandas as pd


class read_file:
    file_path = "D:\\AAA  Studies\\Semester II\\DATA MINING\\Datasets\\output.json"
    data_frame="" 
    filename, file_extension = os.path.splitext(file_path)
   # def set_name(self, name):
     #   self.__prv_name = name
    def read_csv_or_text(self):
        self.data_frame = pd.read_csv(self.file_path) #reading  csv data
        return self.data_frame #return data frame of csv file
    def reading_excel_xls(self):
        import xlrd
        workbook = xlrd.open_workbook(self.file_path)
        #worksheet = workbook.sheet_by_name('titanic3')   #hardcoded
        worksheet = workbook.sheet_by_index(0) #1st sheet value
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
        print(jdata)
        
        #from pandas.io.json import json_normalize    to normalized
        return jdata

#def reading_xml(self): 
   # def reading_text(self):
    def read_clipboard(self):
        clip_data = pd.read_clipboard()
        return clip_data
        #A B C
#x 1 4 p
#y 2 5 q
#z 3 6 r
    def read_html(self):
        import html5lib   #'''pip install pandas pip install lxml pip install html5lib pip install BeautifulSoup4    
        url = 'http://www.fdic.gov/bank/individual/failed/banklist.html'
        data = pd.read_html(url)
        print(data)
       
    #def read_sql(self):
        #data = pd.read_sql()      

obj1 = read_file()
df = obj1.reading_json()
print(df)
#%%

class Write_file():
     input_file = "D:\\AAA  Studies\\Semester II\\DATA MINING\\Datasets\\adult.csv"
     output_file = 'D:\\AAA  Studies\\Semester II\\DATA MINING\\Datasets\\output.json'
     
     def write_csv_to_json(self):
        import csv
        import json
        # Open the CSV  
        f = open(self.input_file , 'rU' )  
        # Change each fieldname to the appropriate field name. I know, so difficult.  
        reader = csv.DictReader( f, fieldnames = ( "fieldname0","fieldname1","fieldname2","fieldname3" ))  
        # Parse the CSV into JSON  
        out = json.dumps( [ row for row in reader ] )  
        # Save the JSON  
        f = open(self.output_file, 'w')  
        f.write(out)  
        return self.output_file


obj_write = Write_file()
obj_write.write_csv_to_json()

#df = obj1.reading_json()
#print(df)
