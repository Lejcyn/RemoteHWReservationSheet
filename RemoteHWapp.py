import os,re
from os import name
from Supportive import *
import schedule,time
import time

ResSheet21=r"G:\My Drive\Reservation Sheets\Reservation Sheet 2021.xlsx"
ResSheet22=r"G:\My Drive\Reservation Sheets\Reservation Sheet 2022.xlsx"

WorkingWeeks21 = GetWrokingWeeks(2021)
WorkingWeeks22 = GetWrokingWeeks(2022)

LogName='IPListPXI.txt'
IPlistTXT=["IPListPXI.txt"]

Devices =["PXIe TOP 0","00-80-2F-19-D9-56"],["PXIe TOP 1","00:80:2F:19:D9:57"],["PXIe middle-0","00-80-2F-14-41-53"],["PXIe middle-1","00-80-2F-14-41-54"],["PXIe Bottom 0","00:80:2F:12:DF:2C"],["PXIe Bottom 1","00-80-2F-12-DF-2B"],["cRIO 9037-LIB 0","00:80:2F:23:9B:8A"],["cRIO 9037-LIB 1","00:80:2F:23:9B:8B"],["cRIO 9037-TSE 0","00:80:2F:25:FC:56"],["cRIO 9037-TSE 1","00:80:2F:25:FC:57"]
for idx,val in enumerate(Devices):
    Devices[idx][1]=val[1].replace(":","-") 


def job():
    print("Please do not turn off, Remote Hardaware checking in progress")

    PingTargets(2,50)

    ListOfDevices=InitDevices(Devices)

    WriteIPtoFile(LogName,ListOfDevices)
    
    IPList=GetCurrentIPs(IPlistTXT)
    print(IPList)
    UpdateIPs(ResSheet21,WorkingWeeks21,IPList)
    UpdateIPs(ResSheet22,WorkingWeeks22,IPList)
    
#CreateExcel(ResSheet21,WorkingWeeks21)
#CreateExcel(ResSheet22,WorkingWeeks22)
job()
schedule.every(30).minutes.do(job)
# schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)
#schedule.every(30).seconds.do(job)
while 1:
    schedule.run_pending()
    time.sleep(1)