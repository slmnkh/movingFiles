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
    if stInd - len(catchString) - 1 < 0: # this means the folder is calibration data and can be skipped (i-e catchString was not found)
        continue 
    
    driveNum = int(fname[stInd:stInd+4]) 
    month = int(fname[5:7])
    date = int(fname[8:10])
    
    if month == 9 and date == 26: # date mapping
        day = 1
    elif month == 9 and date == 28:
        day = 2
    elif month == 9 and date == 29:
        day = 3
    elif month== 9 and date == 30:
        day= 4
    elif month == 10 and date == 3:
        day = 5
        
    # if folder [D_day][Dr_drive] does not exist, make it
        
    folderName = "[D"+str(day)+"][DR%.02d]/"%driveNum

    if os.path.exists(path+folderName) is False:
        os.system("sudo mkdir "+path+folderName)        
#        os.mkdir(path+folderName)
    
    os.system("sudo cp "+path+fname+" "+path+folderName+fname);
    
    
    
    