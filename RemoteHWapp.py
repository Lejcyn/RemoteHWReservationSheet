import os,re
from os import name
from Supportive import *
import schedule,time
import time




ResSheet21=r"C:\Users\tkowalc\OneDrive - National Instruments\Remote HW reserv\Reservation Sheet 2021.xlsx"
ResSheet22=r"C:\Users\tkowalc\OneDrive - National Instruments\Remote HW reserv\Reservation Sheet 2022.xlsx"

WorkingWeeks21 = GetWrokingWeeks(2021)
WorkingWeeks22 = GetWrokingWeeks(2022)

LogName='IPListPXI.txt'
IPlistTXT=["IPListPXI.txt"]

Devices =["PXIe TOP 0","00-80-2F-19-D9-56"],["PXIe TOP 1","00:80:2F:19:D9:57"],["PXIe middle-0","00-80-2F-14-41-53"],["PXIe middle-1","00-80-2F-14-41-54"],["PXIe Bottom 0","00:80:2F:12:DF:2C"],["PXIe Bottom 1","00-80-2F-12-DF-2B"],["cRIO 9037-LIB 0","00:80:2F:23:9B:8A"],["cRIO 9037-LIB 1","00:80:2F:23:9B:8B"],["cRIO 9037-TSE 0","00:80:2F:25:FC:56"],["cRIO 9037-TSE 1","00:80:2F:25:FC:57"]



def job():
    print("Please do not turn off, Remote Hardaware checking in progress")

    for idx,val in enumerate(Devices):
        Devices[idx][1]=val[1].replace(":","-") 

    PingTargets(2,50)

    ListOfDevices=InitDevices(Devices)

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
    
    IPList=GetCurrentIPs(IPlistTXT)
    print(IPList)
    UpdateIPs(ResSheet21,WorkingWeeks21,IPList)
    UpdateIPs(ResSheet22,WorkingWeeks22,IPList)
    
CreateExcel(ResSheet21,WorkingWeeks21)
CreateExcel(ResSheet22,WorkingWeeks22)
job()
#schedule.every(10).minutes.do(job)
# schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)
schedule.every(16).seconds.do(job)
while 1:
    schedule.run_pending()
    time.sleep(1)