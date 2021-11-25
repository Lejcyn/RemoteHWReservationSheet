# import os
import re
import subprocess
import os
from Supportive import *
# f= os.popen('arp -a') 
# for ip in range(2,50):
#     res=os.popen(f"ping 10.92.1.{ip} -w 1000 -n 1")# For office
#     #res=os.popen(f"ping 10.92.6.{ip} -w 1000 -n 1")#For AE Lib
# Devices =["PXIe Bottom","00:80:2F:12:DF:2C"],["HUBUDPXIE8880 TOP1","00-80-2F-19-D9-56"],["HUBUDPXIE8880 TOP2","00:80:2F:19:D9:57"],["NI-cRIO-9054-0","00:80:2F:22:D3:3A"],["NI-cRIO-9054-1","00:80:2F:22:D3:3B"],["NI-sbRIO-9607-0","00:80:2F:16:F3:4E"],["NI-sbRIO-9607-1","00:80:2F:16:F3:4F"],["cRIO9037TSE-0","00:80:2F:25:FC:56"],["cRIO9037TSE-1","00:80:2F:25:FC:57"],["cRIO9037LIB","00:80:2F:23:9B:8B"],["NI-PXI Bottom","00-80-2F-12-DF-2B"],["NI-cRIO-9036-PLU-0","00:80:2F:21:43:AE"],["NI-cRIO-9036-PLU-1","00:80:2F:21:43:AF"]
# for idx,val in enumerate(Devices):
#     Devices[idx][1]=val[1].replace(":","-") 

# print(Devices)
#---------------------------------------------------------------------------
# import schedule
# import time

# def job():
#     print("I'm working...")
# schedule.every(1).seconds.do(job)

# # schedule.every(1).minutes.do(job)
# # schedule.every().hour.do(job)
# # schedule.every().day.at("10:30").do(job)

# while 1:
#     schedule.run_pending()
#     time.sleep(1)
#--------------------------------------------------------------------
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
gauth = GoogleAuth()           
drive = GoogleDrive(gauth)  


# gfile = drive.CreateFile({'parents': [{'id': '1KFQKPjpUvJdV4SAmN_z6XzIWhuKJeDMO'}]})
# # #Read file and set it as the content of this instance.
# gfile.SetContentFile('IPListPC.txt')
# gfile.Upload() # Upload the file.

# print(gfile['id'])
# # Initialize GoogleDriveFile instance with file id.
# file6 = drive.CreateFile({'id': gfile['id']})
# file6.GetContentFile('catlove.txt') # Download file as 'catlove.png'.


RawFolderID='1KFQKPjpUvJdV4SAmN_z6XzIWhuKJeDMO'
LogName='IPListPC.txt'

FolderID='"'+RawFolderID+'"'
Fstring=FolderID+" in parents and trashed=false"


#Delete all files so far
file_list = drive.ListFile({'q': Fstring}).GetList()
for file in file_list:
    print (file['id'])
    tempfile=drive.CreateFile({'id': file['id']})
    tempfile.Delete()

#Upload Actual file
gfile = drive.CreateFile({'parents': [{'id': RawFolderID}]})
gfile.SetContentFile(LogName)
gfile.Upload() # Upload the file.