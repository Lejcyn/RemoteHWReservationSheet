import os,re
from ListOfMACAdress import *
open('IPList.txt', 'w').close()
Tfile = open("IPList.txt", "r+")
Tfile.truncate(0) # need '0' when using r+
f= os.popen('arp -a') 
data = f.read()
#Name= [IPadress,MAC]
ListOfDevices=InitDevices()
for line in re.findall('([-.0-9]+)\s+([-0-9a-f]{17})\s+(\w+)',data):
  for device in ListOfDevices:
    if line[1] == device.getMAC():
      device.IPadress=line[0]

for dev in ListOfDevices:
    dev.printout()
    Tfile.writelines(dev.Name+dev.MAC+dev.IPadress)
   
Tfile.close()
print("Done")
