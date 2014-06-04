

import os




path = "/home/skhokhar/Downloads/";
savePath = "/home/skhokhar/common/people/skhokhar/";

i = 0;

for file in os.listdir(path):
    
    if file.startswith("2011"):
       
        i=i+1;
        print "Copying file "+file+" ... file number: %d"%i;
        os.system("sudo cp "+path+file+" "+savePath+file);
  
      