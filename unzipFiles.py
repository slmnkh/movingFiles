# -*- coding: utf-8 -*-
"""
Created on Wed Jun  4 10:14:20 2014

@author: skhokhar
"""
import os

path = "/home/skhokhar/common/people/skhokhar/KITTI/Residential/"

savePath = "/home/skhokhar/common/people/skhokhar/KITTI/residentialUnzipped/"

list = os.listdir(path)
i = 0
for fname in list:
    

    if os.path.exists(savePath+fname[0:-4]) is False:

	    os.system("sudo mkdir "+savePath+"/"+fname[0:-4])
	    os.system("sudo unzip "+path+fname+" -d "+savePath+fname[0:-4])
	    i = i + 1
	    print "Folder %d"%i+" done" 


