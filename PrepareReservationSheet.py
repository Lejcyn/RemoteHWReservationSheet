import pandas as pd
import xlsxwriter
from Supportive import *
from ClassDeclare import *
IPlistTXT=["IPListPC.txt","IPListPXI.txt"]

ResSheet=r"C:\Users\tkowalc\OneDrive - National Instruments\Remote HW reserv\Draft Reservation Sheet.xlsx"
WorkingWeeks = GetWrokingWeeks()

CreateExcel(ResSheet,WorkingWeeks)
#Static IP list for maintaining Excel layout
IPList=["PXIe TOP","10.92.6.29"],["PXIe Middle","10.92.6.55"],["PXIe Bottom","110.92.6.29"],["cRIO 9037-LIB","10.92.6.29"],["cRIO 9037-TSE","NO IP"]


NewIPList= ReadIPList(IPlistTXT)

for idx,dev in enumerate(IPList):
    for i,newdev in enumerate(NewIPList):
        if dev[0]in newdev[0]:
            dev[1]= newdev[2]

print(IPList)
UpdateIPs(ResSheet,WorkingWeeks,IPList)