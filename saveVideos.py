# -*- coding: utf-8 -*-
"""
Created on Thu Jun  5 14:06:50 2014

@author: skhokhar
"""

import os

scenePath = "/home/skhokhar/common/people/skhokhar/KITTI/unzipped/roadUnzipped"
path = scenePath+"/synced/"
savePath = scenePath+"/synced_videos/"

if os.path.exists(savePath) is False:
    
    os.system("sudo mkdir "+savePath)
    
list = os.listdir(path)
i= 0
for fname in list:
    i = i +1
    os.system("sudo convert -quality 100 -delay 10 "+path+fname+"/image_02/data/*.png "+savePath+fname+".mpeg")
    print "Done with video: %d"%i
    
