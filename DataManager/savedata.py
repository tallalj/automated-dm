import csv
import json
import pandas as pd
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class savedata(QWidget):


    def write_csv_to_json(self, csvFilePath, jasonFilePath):
        # Open the CSV
        f = open(self.input_file, 'rU')
        # Change each fieldname to the appropriate field name. I know, so difficult.
        reader = csv.DictReader(f, fieldnames=("fieldname0", "fieldname1", "fieldname2", "fieldname3"))
        # Parse the CSV into JSON
        out = json.dumps([row for row in reader])
        # Save the JSON
        f = open(self.output_file, 'w')
        f.write(out)
        return self.output_file

    def writeCSV(self, dataFrame: pd.DataFrame):
        """writes the data frame in csv format"""
        #fileName = QFileDialog.getSaveFileName(self,'Save file','c:\\',"dataFile (*.*)")
        fname = QFileDialog.getSaveFileName(self, 'Save file','c:\\', "Image files (*.csv)")
        print(dataFrame.dtypes)
        dataFrame.to_csv(fname)

    def writeJSON(self, dataFrame: pd.DataFrame):
        """writes the data frame in json format"""
        fname = QFileDialog.getSaveFileName(self, 'Save file', 'c:\\', "Image files (*.json)")
        dataFrame.to_json(fname)