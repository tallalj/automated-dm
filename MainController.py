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
import sys
from DataManager.savedata import savedata
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

def clear_table(self):
 global Obj_analize
 Obj_analize.selected(dataset,window,3)
 return
def cell(row, column):
    print("Row %d and Column %d was clicked" % (row, column))
    Obj_analize.selected(dataset,window,row)

def Exit(self):
    sys.exit()
def Aboutus():
   msg = QMessageBox()
   msg.setIcon(QMessageBox.Information)

   msg.setText("Design by ITU")
   msg.setInformativeText("")
   msg.setWindowTitle("About Us")
   msg.setDetailedText("Tabish Manzoor\nTallal Javed\nMubashir imran\nTaila Jabeen")
   msg.setStandardButtons(QMessageBox.Ok)

   retval = msg.exec_()
app = QtGui.QApplication(sys.argv)
window = uic.loadUi("mainview.ui")
window.show()
#/--------------------------------------------- Menu Controll  -----------------------------------------/
def Json(self):
    sv = savedata()
    sv.writeJSON(dataset)

def XML(self):
    print("work in progress")
def CSV(self):
    sv = savedata()
    sv.writeCSV(dataset)

#/--------------------------------------------- Menu Controll  -----------------------------------------/


Obj_analize=AndlizeData()
outliers_processor=Outlier()
window.edDatapathbutton.clicked.connect(get_File)
window.analize.clicked.connect(start_analize)
window.clear.clicked.connect(clear_table)
window.ColDetail.cellClicked.connect(cell)


window.actionOpen.triggered.connect(get_File)
window.actionExit.triggered.connect(Exit)

window.actionAbout_help.triggered.connect(Aboutus)

window.actionJSon.triggered.connect(Json)
window.actionXML.triggered.connect(XML)
window.actionCSV.triggered.connect(CSV)


sys.exit(app.exec_())
