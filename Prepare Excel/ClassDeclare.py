
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

