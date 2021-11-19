import pandas as pd
import xlsxwriter
from Supportive import *

WorkingWeeks = GetWrokingWeeks()
df = pd.read_excel(r"Prepare Excel\dfTemplate.xlsx")
print(df)
writer=pd.ExcelWriter(r"C:\Users\tkowalc\OneDrive - National Instruments\Remote HW reserv\Draft Reservation Sheet.xlsx",engine='xlsxwriter')
workbook  = writer.book

for week in WorkingWeeks:
    df.to_excel(writer,index=False,startcol=0,startrow = 1, sheet_name=week)    
    df.to_excel(writer,index=False,startcol=7,sheet_name=week)
    merge_format = workbook.add_format({
        'bold': 1,
        'border': 1,
        'align': 'center',
        'valign': 'vcenter'})

    worksheet = writer.sheets[week]
    worksheet.merge_range("B1:F1","Device1", merge_format)
writer.close()
workbook.close()

