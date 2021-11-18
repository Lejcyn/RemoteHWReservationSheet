import pandas as pd
import xlsxwriter


df = pd.read_excel(r"Prepare Excel\dfTemplate.xlsx")
print(df)
writer=pd.ExcelWriter(r"C:\Users\tkowalc\OneDrive - National Instruments\Remote HW reserv\Draft Reservation Sheet.xlsx",engine='xlsxwriter')
weeks=["1","2","3"]
for week in weeks:
    df.to_excel(writer,index=False,startcol=0,startrow = 1, sheet_name=week)
    df.to_excel(writer,index=False,startcol=7,sheet_name=week)
workbook  = writer.book
worksheet = writer.sheets['1']

merge_format = workbook.add_format({
    'bold': 1,
    'border': 1,
    'align': 'center',
    'valign': 'vcenter'})

worksheet.merge_range("B1:F1","Device1", merge_format)
writer.close()
workbook.close()

