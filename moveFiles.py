

import os




path = "/home/skhokhar/Downloads/";
savePath = "/home/skhokhar/Datasets/KITTI/Residential/";

if os.path.exists(savePath) is False:
    os.system("sudo mkdir "+savePath) 

i = 0;

for file in os.listdir(path):
    
    if file.startswith("2011") and file.endswith("extract.zip") is False:
       
        i=i+1;
        print "Copying file "+file+" ... file number: %d"%i;
        os.system("sudo cp "+path+file+" "+savePath+file);
  
      
