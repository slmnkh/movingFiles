# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
/home/skhokhar/.spyder2/.temp.py
"""

import os


path = "/home/skhokhar/common/people/skhokhar/2011_09_26/"
catchString = "drive"
list = os.listdir(path) # find all folders in path

for fname in list: # for each folder
    
    stInd = fname.find(catchString)+len(catchString)+1 # find location of catchString 
    if stInd < 0: # this means the folder is calibration data and can be skipped
        continue
    
    driveNum = int(fname[stInd:stInd+4]) 
    month = int(fname[5:7])
    date = int(fname[8:10])
    
    if month == 09 and date == 26: # date mapping
        day = 1
    elif month == 09 and date == 28:
        day = 2
    elif month == 09 and date == 29:
        day = 3
    elif month== 09 and date == 30:
        day= 4
    elif month == 10 and date == 03:
        day = 5
        
    # if folder [D_day][Dr_drive] does not exist, make it
        
    folderName = "[D"+str(day)+"][DR%.02d"driveNum
    if !os.path.exists(path+folderName):
        mkdir()
    
    
    
    