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

class Outlier:
 total_rows="";
 number_of_columns_outliers=""
 number_of_rows_outliers=""
 def start(self,dataset,window):
  for count in range(0, len(dataset.columns)):
   cell=dataset[dataset.columns[count]]
   print("---------------------------------")
   print(len(cell))
  return