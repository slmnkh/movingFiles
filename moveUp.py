# -*- coding: utf-8 -*-
"""
Created on Thu Jun  5 11:06:38 2014

@author: skhokhar
"""

import os

path = "/home/skhokhar/common/people/skhokhar/KITTI/unzipped/personUnzipped/synced/";

list = os.listdir(path)

for fname in list:
    
    os.system("sudo mv "+path+fname+"/"+fname[0:10]+"/"+fname+"/* "+path+fname+"/")
    os.system("sudo rm -r "+path+fname+"/"+fname[0:10])