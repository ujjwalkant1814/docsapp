# -*- coding: utf-8 -*-
"""
@author: kantu
"""


import pandas as pd
import glob

#Importing Data
files = glob.glob("Health-Tweets/*.txt")

data = pd.DataFrame({})
for i in files:
    try:
        data_i = pd.read_csv(i, 
                             sep ="|", 
                             header =  None,
                             error_bad_lines = False)
    except UnicodeDecodeError:
        print("Using ISO-8859-1 encoding for %s"%(i))
        data_i = pd.read_csv(i, 
                             sep ="|", 
                             header =  None,
                             error_bad_lines = False,
                             encoding = "ISO-8859-1")
    data = pd.concat([data, data_i], axis = 0)
 
#lets rename the columns of the data
data.columns = ['ID','Date','Comment']
    
