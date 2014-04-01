#fun timeing clean the downloads dir

#!/usr/bin/python

import os
import time
import shutil

dir="/Users/psnail/Downloads/"
current=time.time()
dirlist=os.listdir(dir)
for line in dirlist:
	if line.find('.') == 0 :
		continue
	file=dir+line
	gettime=os.path.getctime(file)

	# file days ago and del it
	if  int(current) - int(gettime) > 60*60*24*30:
		if os.path.isdir(file):
			shutil.rmtree(file,True)
		else :
			os.remove(file)
