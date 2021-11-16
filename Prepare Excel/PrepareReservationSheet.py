import pandas as pd


df = pd.read_excel(r"Prepare Excel\dfTemplate.xlsx")
print(df)
writer=pd.ExcelWriter(r"C:\Users\tkowalc\OneDrive - National Instruments\Remote HW reserv\Draft Reservation Sheet.xlsx",engine='xlsxwriter')
weeks=["1","2","3"]
for week in weeks:
    df.to_excel(writer,index=False,startcol=0,sheet_name=week)
    df.to_excel(writer,index=False,startcol=7,sheet_name=week)

writer.close()

