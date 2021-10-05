from os import name

Devices =["HUBUDPXIE8880 TOP","00-80-2F-19-D9-56"],["cRIO9037TSE","00:80:2F:25:FC:57"],["cRIO9037LIB","00:80:2F:23:9B:8B"],["NI-PXI Bottom","00-80-2F-12-DF-2B"]
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

#ConstructorTest
# Test=InitDevices()

# for dev in Test:
#     dev.printout()

