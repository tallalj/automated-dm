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

from GetData import GetData
from AndlizeData import AndlizeData
from Outlier import Outlier
from PreProcessing.sanitizor import sanitizor
dataset="";


def get_File(self):
 Data=GetData()
 global dataset
 dataset=Data.get_File(window)

def start_analize(self):
 global dataset
 global window
 global Obj_analize
 global outliers_processor
 Obj_analize.start(dataset,window)
 outliers_processor.start(dataset,window)
 Obj_sanitizor=sanitizor()
 result = Obj_sanitizor.analyze_df(dataset);
 window.dataframesummery.setText(result)
def clear_table(self):
 global Obj_analize
 #Obj_analize.selected(dataset,window,3)

 return
def cell(row, column):
    global dataset
    global window
    print("Row %d and Column %d was clicked" % (row, column))
    Obj_analize.selected(dataset,window,row)
    Obj_sanitizor=sanitizor()
    result = Obj_sanitizor.analyze_col(dataset.ix[:,row]);
    window.cellsummery.setText(result)
    cellsummery
app = QtGui.QApplication(sys.argv)
window = uic.loadUi("mainview.ui")

window.show()


Obj_analize=AndlizeData()
outliers_processor=Outlier()
window.Datapathbutton.clicked.connect(get_File)
window.analize.clicked.connect(start_analize)
window.clear.clicked.connect(clear_table)
window.ColDetail.cellClicked.connect(cell)

sys.exit(app.exec_())
