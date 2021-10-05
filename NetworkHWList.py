import os,re
from ListOfMACAdress import *
f= os.popen('arp -a') 
data = f.read()
#Name= [IPadress,MAC]
ListOfDevices=InitDevices()
for line in re.findall('([-.0-9]+)\s+([-0-9a-f]{17})\s+(\w+)',data):
  for device in ListOfDevices:
    if line[1] == device.getMAC():


print("done")