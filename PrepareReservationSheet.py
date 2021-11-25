import pandas as pd
import xlsxwriter
from Supportive import *
from ClassDeclare import *
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
gauth = GoogleAuth()           
drive = GoogleDrive(gauth)  

#For PC
file_list = drive.ListFile({'q': "'1KFQKPjpUvJdV4SAmN_z6XzIWhuKJeDMO' in parents and trashed=false"}).GetList()
for file in file_list:
    file6 = drive.CreateFile({'id': file['id']})
file6.GetContentFile('IPListPC.txt') # Download file 
#For PXI
file_list = drive.ListFile({'q': "'1cG_tS0eSLqb63O8r65cHyl6qJ8UUgS6A' in parents and trashed=false"}).GetList()
for file in file_list:
    file6 = drive.CreateFile({'id': file['id']})
file6.GetContentFile('IPListPXI.txt') # Download file 


IPlistTXT=["IPListPC.txt","IPListPXI.txt"]

ResSheet=r"C:\Users\tkowalc\OneDrive - National Instruments\Remote HW reserv\Reservation Sheet 2022.xlsx"
#ResSheet=r"C:\Users\tkowalc\OneDrive - National Instruments\Remote HW reserv\Reservation Sheet 2021.xlsx"

WorkingWeeks = GetWrokingWeeks()

#CAREFUL
#CreateExcel(ResSheet,WorkingWeeks)# CAREFUL WITH THIS CALL< ITS OVERWRITING
#CAREFUL

#Static IP list for maintaining Excel layout
IPList=["PXIe TOP","10.92.6.29"],["PXIe Middle","10.92.6.55"],["PXIe Bottom","110.92.6.29"],["cRIO 9037-LIB","10.92.6.29"],["cRIO 9037-TSE","NO IP"]


NewIPList= ReadIPList(IPlistTXT)

for idx,dev in enumerate(IPList):
    for i,newdev in enumerate(NewIPList):
        if dev[0]in newdev[0]:
            dev[1]= newdev[2]

print(IPList)
UpdateIPs(ResSheet,WorkingWeeks,IPList)