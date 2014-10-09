#!/usr/bin/python
import os
import time
source='/home/tcpdemo/test'
target='/home/'
today=target+time.strftime('%Y%m%d')
targetfile=today+'.zip'
zip_command="zip -qr %s %s"%(targetfile,''.join(source))
os.system(zip_command)
