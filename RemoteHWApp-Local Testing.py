
from Supportive import *
import schedule,time

ResSheet21=r"C:\Users\HUBUDPXIe-8880\OneDrive\Reservation Sheet 2021.xlsx"
WorkingWeeks21 = GetWrokingWeeks(2021)

ResSheet22=r"C:\Users\HUBUDPXIe-8880\OneDrive\Reservation Sheet 2022.xlsx"
WorkingWeeks22 = GetWrokingWeeks(2022)

IPlistTXT=["IPListPXI.txt"]

def job():

    IPList=GetCurrentIPs(IPlistTXT)
    print(IPList)
    UpdateIPs(ResSheet21,WorkingWeeks21,IPList)
    UpdateIPs(ResSheet22,WorkingWeeks22,IPList)


job()
#schedule.every(30).minutes.do(job)
schedule.every(1).hour.do(job)
# schedule.every().day.at("10:30").do(job)
#schedule.every(20).seconds.do(job)
while 1:
    schedule.run_pending()
    time.sleep(1)

#CAREFUL
#CreateExcel(ResSheet,WorkingWeeks)# CAREFUL WITH THIS CALL< ITS OVERWRITING
#CAREFUL


