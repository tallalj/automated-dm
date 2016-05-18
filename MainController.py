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
from DataManager.savedata import savedata

from GetData import GetData
from AndlizeData import AndlizeData
from Outlier import Outlier

dataset = "";

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
    return

# Export logic
def selectionchange(self):
    " asdasd"

def exportButtonPressed(self):
    print(GetData.filePath)

    savedata().writeCSV(GetData.dataFrame)

app = QtGui.QApplication(sys.argv)
window = uic.loadUi("mainview.ui")

window.show()
Obj_analize=AndlizeData()
outliers_processor=Outlier()
window.Datapathbutton.clicked.connect(get_File)
window.analize.clicked.connect(start_analize)
window.clear.clicked.connect(clear_table)
window.exportButton.clicked.connect(exportButtonPressed)
sys.exit(app.exec_())
