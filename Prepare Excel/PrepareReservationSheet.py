import pandas as pd
import xlsxwriter
from Supportive import *

WorkingWeeks = GetWrokingWeeks()
df = pd.read_excel(r"Prepare Excel\dfTemplate.xlsx")
writer=pd.ExcelWriter(r"C:\Users\tkowalc\OneDrive - National Instruments\Remote HW reserv\Draft Reservation Sheet.xlsx",engine='xlsxwriter')
workbook  = writer.book
merge_format = workbook.add_format({
        'bold': 1,
        'border': 1,
        'align': 'center',
        'valign': 'vcenter'})
for week in WorkingWeeks:
    df.to_excel(writer,index=False,startcol=0,startrow = 1, sheet_name=week)    
    df.to_excel(writer,index=False,startcol=7,startrow = 1, sheet_name=week)
    df.to_excel(writer,index=False,startcol=14,startrow = 1, sheet_name=week)
    df.to_excel(writer,index=False,startcol=21,startrow = 1, sheet_name=week)
    df.to_excel(writer,index=False,startcol=28,startrow = 1, sheet_name=week)
    worksheet = writer.sheets[week]
    worksheet.merge_range("B1:F1","Device1", merge_format)
    worksheet.merge_range("H1:M1","Device2", merge_format)
    worksheet.merge_range("O1:T1","Device3", merge_format)
    worksheet.merge_range("V1:AA1","Device4", merge_format)
    worksheet.merge_range("AC1:AH1","Device5", merge_format)
writer.close()
workbook.close()

