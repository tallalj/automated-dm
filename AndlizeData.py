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
import matplotlib.pyplot as plot2

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas



class AndlizeData:
 def start(self,dataset,window):
  window.ColDetail.setRowCount(len(dataset.columns));
  for count in range(0, len(dataset.columns)):
   Col1_Number =count + 1
   Col2_ColName=dataset.columns[count]
   cell=dataset[dataset.columns[count]]
   Col3_type=cell.dtype.name
   Col4_na=self.Find_Missing_values(cell)
   Col5_var=len(cell.unique())
   if Col3_type!='object':
    #------------------------------------------------------------------------------------------------
    plt.boxplot(cell)
    boxplot = plt.gcf()
    boxplot.savefig('boxplot.png', dpi=100)
    pixmaxboxplot=QtGui.QPixmap('boxplot.png')
    pixmaxboxplot=pixmaxboxplot.scaled(531, 361)

    window.plot.setPixmap(pixmaxboxplot)
    plt.close(boxplot)
   #------------------------------------------------------------------------------------------------

    plt.scatter(cell.index, cell)
    figure_scatter2 = plt.gcf()
    figure_scatter2.savefig('figure_scatter.png', dpi=100)
    pixmax=QtGui.QPixmap('figure_scatter.png')
    pixmax=pixmax.scaled(681, 471)
    window.visulization.setPixmap(pixmax)

   #------------------------------------------------------------------------------------------------

   item1 = QTableWidgetItem(str(Col1_Number))
   item2 = QTableWidgetItem(str(Col2_ColName))
   item3 = QTableWidgetItem(str(Col3_type))
   item4 = QTableWidgetItem(str(Col4_na))
   item5 = QTableWidgetItem(str(Col5_var))
   item1.setFlags(QtCore.Qt.ItemIsEnabled )
   item2.setFlags(QtCore.Qt.ItemIsEnabled )
   item3.setFlags(QtCore.Qt.ItemIsEnabled )
   item4.setFlags(QtCore.Qt.ItemIsEnabled )
   item5.setFlags(QtCore.Qt.ItemIsEnabled )

   window.ColDetail.setItem(count,0,item1)
   window.ColDetail.setItem(count,1,item2)
   window.ColDetail.setItem(count,2,item3)
   window.ColDetail.setItem(count,3,item4)
   window.ColDetail.setItem(count,4,item5)


  return
 def selected(self,dataset,window,row):
  window.ColDetail.setRowCount(len(dataset.columns));
  cell=dataset[dataset.columns[row]]
  Ctype=cell.dtype.name
  if Ctype!='object':
   #------------------------------------------------------------------------------------------------
   plt.boxplot(cell)
   boxplot = plt.gcf()
   boxplot.savefig('boxplot.png', dpi=100)
   pixmaxboxplot=QtGui.QPixmap('boxplot.png')
   pixmaxboxplot=pixmaxboxplot.scaled(531, 361)
   window.plot.setPixmap(pixmaxboxplot)
   plt.close(boxplot)
   #------------------------------------------------------------------------------------------------
   plt.scatter(cell.index, cell)
   figure_scatter2 = plt.gcf()
   figure_scatter2.savefig('figure_scatter.png', dpi=100)
   pixmax=QtGui.QPixmap('figure_scatter.png')
   pixmax=pixmax.scaled(681, 471)
   window.visulization.setPixmap(pixmax)
  #------------------------------------------------------------------------------------------------

  return
 def Find_Missing_values(self,DataCol):
     data=pd.isnull(DataCol)
     number_of_nas=0;
     for count in range(0, len(data)):
         if data[count]==True:
             number_of_nas=number_of_nas+1;
     return number_of_nas

