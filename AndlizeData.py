import sys
from PyQt4 import QtGui, uic ,QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import pandas as pd
import numpy as np
import copy
import math
import random
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
class AndlizeData:
 def start(self,dataset,window):
  window.ColDetail.setRowCount(len(dataset.columns));
  for count in range(0, len(dataset.columns)):
   Col1_Number =count + 1
   Col2_ColName=dataset.columns[count]
   cell=dataset[dataset.columns[count]]
   Col3_type=cell.dtype.name
   print(cell.dtype)
   Col4_na=self.Find_Missing_values(cell)
   Col5_var=len(cell.unique())
   if Col3_type!='object':
    plt.boxplot(cell)

    figure=plt.figure()
    canv = FigureCanvas(figure)
    hBoxLayout	 = QHBoxLayout()
    hBoxLayout.setObjectName("boxImage")
    hBoxLayout.setGeometry(QRect(100, 100, 100, 100))
    hBoxLayout.addWidget(canv)

    window.plot.setLayout(hBoxLayout)
    print("************************")
    print(type(figure))

    #window.plot.setPixmap(figure)
   print(Col1_Number,Col2_ColName,Col3_type,Col4_na,Col5_var)
   item1 = QTableWidgetItem(str(Col1_Number))
   item2 = QTableWidgetItem(str(Col2_ColName))
   item3 = QTableWidgetItem(str(Col3_type))
   item4 = QTableWidgetItem(str(Col4_na))
   item5 = QTableWidgetItem(str(Col5_var))

   window.ColDetail.setItem(count,0,item1)
   window.ColDetail.setItem(count,1,item2)
   window.ColDetail.setItem(count,2,item3)
   window.ColDetail.setItem(count,3,item4)
   window.ColDetail.setItem(count,4,item5)


  return
 def Find_Missing_values(self,DataCol):
     data=pd.isnull(DataCol)
     number_of_nas=0;
     for count in range(0, len(data)):
         if data[count]==True:
             number_of_nas=number_of_nas+1;
     return number_of_nas

