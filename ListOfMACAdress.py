Devices =["HUBUDPXIE8880","01-00-5e-00-00-16"],["cRIO9037TSE","00:80:2F:25:FC:57"],["cRIO9037LIB","00:80:2F:23:9B:8B"]
class Device:
   
    def __init__(Name,MAC):
        self.IPadress="NO IP"
        self.Name=""
        self.MAC=""

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
        dlist.append(Device(device[0]),device[1])
    return(dlist)


Test=InitDevices()

for dev in Test:
    dev.printout()