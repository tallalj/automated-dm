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

from DataManager.loaddata import loaddata

dataset="";

class GetData(QtGui.QFileDialog):
 def get_File(self,window):
  """Gets the path of the file selected via file picker"""
  DataSetPath = self.getOpenFileName(self,'Open file','c:\\',"dataFile (*.*)")
  window.DataPath.setText(DataSetPath)
  #RowData=pd.read_csv(DataSetPath,low_memory=False)
  ld = loaddata()
  RowData = ld.read_file_at_path(DataSetPath)
  print(len(RowData.columns))
  return RowData