import os,re
from os import name
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


Devices =["PXIe middle-0","00-80-2F-14-41-53"],["PXIe middle-1","00-80-2F-14-41-54"],["PXIe Bottom","00:80:2F:12:DF:2C"],["HUBUDPXIE8880 TOP1","00-80-2F-19-D9-56"],["HUBUDPXIE8880 TOP2","00:80:2F:19:D9:57"],["NI-cRIO-9054-0","00:80:2F:22:D3:3A"],["NI-cRIO-9054-1","00:80:2F:22:D3:3B"],["NI-sbRIO-9607-0","00:80:2F:16:F3:4E"],["NI-sbRIO-9607-1","00:80:2F:16:F3:4F"],["cRIO9037TSE-0","00:80:2F:25:FC:56"],["cRIO9037TSE-1","00:80:2F:25:FC:57"],["cRIO9037LIB","00:80:2F:23:9B:8B"],["NI-PXI Bottom","00-80-2F-12-DF-2B"],["NI-cRIO-9036-PLU-0","00:80:2F:21:43:AE"],["NI-cRIO-9036-PLU-1","00:80:2F:21:43:AF"]
for idx,val in enumerate(Devices):
    Devices[idx][1]=val[1].replace(":","-") 


for ip in range(2,50):
    res=os.popen(f"ping 10.92.1.{ip} -w 1000 -n 1")# For office
    #res=os.popen(f"ping 10.92.6.{ip} -w 1000 -n 1")#For AE Lib



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
            check=dev.getName()+"\t"+dev.getMAC()+"\t"+dev.getIP()+"\n"
            Tfile.writelines(check)
Tfile.close()


