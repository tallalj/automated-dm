"""
Created on 5/17/2016

@author: eagle
"""
import pandas as pd
import matplotlib.pyplot as plt

class visualizer:
    def __init__(self):
        print("Initialized visualizer")

    def getHistFor(self, dataFrame, Coloumn):
        print("returns the plot for the given data frames column")
        plt.figure()
        dataFrame.plot.hist(alpha = 0.5)