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

dataset="";

class GetData(QtGui.QFileDialog):
 def get_File(self,window):
  DataSetPath = self.getOpenFileName(self,'Open file','c:\\',"dataFile (*.csv)")
  window.DataPath.setText(DataSetPath)
  RowData=pd.read_csv(DataSetPath,low_memory=False)
  print(len(RowData.columns))
  return RowData
