import os,re
from os import name

import schedule
import time
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
gauth = GoogleAuth()           
drive = GoogleDrive(gauth)  

#For PC

RawFolderID='1KFQKPjpUvJdV4SAmN_z6XzIWhuKJeDMO'
LogName='IPListPC.txt'


#For PXI

#RawFolderID='1cG_tS0eSLqb63O8r65cHyl6qJ8UUgS6A'
#LogName='IPListPXI.txt' for PXI


FolderID='"'+RawFolderID+'"'
Fstring=FolderID+" in parents and trashed=false"

Devices =["PXIe TOP 0","00-80-2F-19-D9-56"],["PXIe TOP 1","00:80:2F:19:D9:57"],["PXIe middle-0","00-80-2F-14-41-53"],["PXIe middle-1","00-80-2F-14-41-54"],["PXIe Bottom 0","00:80:2F:12:DF:2C"],["PXIe Bottom 1","00-80-2F-12-DF-2B"],["cRIO 9037-LIB 0","00:80:2F:23:9B:8A"],["cRIO 9037-LIB 1","00:80:2F:23:9B:8B"],["cRIO 9037-TSE 0","00:80:2F:25:FC:56"],["cRIO 9037-TSE 1","00:80:2F:25:FC:57"]
class Device:

    def __init__(self,name,mac):
        self.IPadress="NO IP"
        self.Name=name
        self.MAC=mac

    def getIP(self):
        return self.IPadress

    def getName(self):
        return self.Name

    def getMAC(self):
        return self.MAC

    def printout(self):
        print(self.getName(),self.getMAC(),self.getIP())

def InitDevices ():
    dlist=[]
    for device in Devices:
        dlist.append(Device(device[0],device[1]))
    return(dlist)

def job():
    print("I'm working...")

    for idx,val in enumerate(Devices):
        Devices[idx][1]=val[1].replace(":","-") 


    for ip in range(2,50):
        res=os.popen(f"ping 10.92.1.{ip} -w 1000 -n 1")# For office
        res=os.popen(f"ping 10.92.6.{ip} -w 1000 -n 1")#For AE Lib


    ListOfDevices=InitDevices()
    #Open File
    open(LogName, 'w+').close()
    Tfile = open(LogName, "r+")
    Tfile.truncate(0) # need '0' when using r+
    #Manage ARP
    f= os.popen('arp -a') 
    data = f.read()
    kek=re.findall('([-.0-9]+)\s+([-0-9a-f]{17})\s+(\w+)',data)
    for line in kek:
        for device in ListOfDevices:
            if line[1].lower() == device.getMAC().lower():
                device.IPadress=line[0]

    #Write to file only found devices
    for dev in ListOfDevices:
            str=dev.getIP()
            if str  != 'NO IP':
                dev.printout()
                check=dev.getName()+","+dev.getMAC()+","+dev.getIP()+"\n"
                Tfile.writelines(check)
    Tfile.close()
    
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




# schedule.every(1).minutes.do(job)
# schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)
schedule.every(10).seconds.do(job)
while 1:
    schedule.run_pending()
    time.sleep(1)