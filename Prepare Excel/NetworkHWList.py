import os,re
from os import name
from ClassDeclare import *
from Supportive import *
Devices =["PXIe TOP 0","00-80-2F-19-D9-56"],["PXIe TOP 1","00:80:2F:19:D9:57"],["PXIe middle-0","00-80-2F-14-41-53"],["PXIe middle-1","00-80-2F-14-41-54"],["PXIe Bottom 0","00:80:2F:12:DF:2C"],["PXIe Bottom 1","00-80-2F-12-DF-2B"],["cRIO 9037-LIB 0","00:80:2F:23:9B:8A"],["cRIO 9037-LIB 1","00:80:2F:23:9B:8B"],["cRIO 9037-TSE 0","00:80:2F:25:FC:56"],["cRIO 9037-TSE 1","00:80:2F:25:FC:57"]

def InitDevices ():
    dlist=[]
    for device in Devices:
        dlist.append(Device(device[0],device[1]))
    return(dlist)


for idx,val in enumerate(Devices):
    Devices[idx][1]=val[1].replace(":","-") 


for ip in range(2,50):
    res=os.popen(f"ping 10.92.1.{ip} -w 1000 -n 1")# For office
    res=os.popen(f"ping 10.92.6.{ip} -w 1000 -n 1")#For AE Lib



ListOfDevices=InitDevices()
#Open File
open('IPList.txt', 'w').close()
Tfile = open("IPList.txt", "r+")
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


