# -*- coding: utf-8 -*-
"""
@author: kantu
"""


import pandas as pd
import glob

files = glob.glob("Health-Tweets/*.txt")

for i in files:
    print(i)
    data = pd.read_csv('Health-Tweets\cbchealth.txt', sep ="|", header =  None)
