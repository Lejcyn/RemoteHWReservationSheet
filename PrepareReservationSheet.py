
from Supportive import *
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import schedule,time
gauth = GoogleAuth()           
drive = GoogleDrive(gauth)  



ResSheet21=r"C:\Users\tkowalc\OneDrive - National Instruments\Remote HW reserv\Reservation Sheet 2021.xlsx"
WorkingWeeks21 = GetWrokingWeeks(2021)

ResSheet22=r"C:\Users\tkowalc\OneDrive - National Instruments\Remote HW reserv\Reservation Sheet 2022.xlsx"
WorkingWeeks22 = GetWrokingWeeks(2022)

IPlistTXT=["IPListPC.txt","IPListPXI.txt"]

def job():
        
    #For PC
    file_list = drive.ListFile({'q': "'1KFQKPjpUvJdV4SAmN_z6XzIWhuKJeDMO' in parents and trashed=false"}).GetList()
    for file in file_list:
        file6 = drive.CreateFile({'id': file['id']})
    file6.GetContentFile('IPListPC.txt') # Download file 
    #For PXIsa
    file_list = drive.ListFile({'q': "'1cG_tS0eSLqb63O8r65cHyl6qJ8UUgS6A' in parents and trashed=false"}).GetList()
    for file in file_list:
        file6 = drive.CreateFile({'id': file['id']})
    file6.GetContentFile('IPListPXI.txt') # Download file 

    IPList=GetCurrentIPs(IPlistTXT)

    print(IPList)
    UpdateIPs(ResSheet21,WorkingWeeks21,IPList)
    UpdateIPs(ResSheet22,WorkingWeeks22,IPList)



job()
schedule.every(30).minutes.do(job)
# schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)
#schedule.every(20).seconds.do(job)
while 1:
    schedule.run_pending()
    time.sleep(1)

#CAREFUL
#CreateExcel(ResSheet,WorkingWeeks)# CAREFUL WITH THIS CALL< ITS OVERWRITING
#CAREFUL


