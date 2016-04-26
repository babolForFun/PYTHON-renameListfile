# !/usr/bin/python

import os
import random
import time
import datetime

def rename_files(path):
    file_list = os.listdir(path)
    ts = time.time()    
    for file_name in file_list:
        if file_name == os.path.basename(__file__):
        	pass
        else:
	        new_file_name = str(datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')) + file_name
	        print(file_name + " ---->  " + new_file_name)
	        os.rename(os.path.join(path, file_name), os.path.join(path, new_file_name))

rename_files('./')