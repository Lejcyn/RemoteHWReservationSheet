import datetime
import pandas as pd
import xlsxwriter # CANNOT BE USED FOR MODIFICATION
import openpyxl
def GetWrokingWeeks():
    FinalList=[]
    def workdays(d, end, excluded=(6, 7)):
        days = []
        while d.date() <= end.date():
            if d.isoweekday() not in excluded:
                days.append(d)
            d += datetime.timedelta(days=1)
        return days
    TotalDays=workdays(datetime.datetime(2022, 1, 2),datetime.datetime(2022, 12, 31))
    LastElem=TotalDays[-1].isocalendar()[1]
    TotalWeeks=[[]for i in range(LastElem)]
    for data in TotalDays:
        weeknum=data.isocalendar()[1]
        TotalWeeks[weeknum-1].append(data) # Tu co nie gra

    for week in TotalWeeks:
        FinalList.append(f"{week[0].day}.{week[0].month}-{week[-1].day}.{week[0].month}")
    return FinalList

def CreateExcel(path,WorkingWeeks):
    df = pd.read_excel(r"Prepare Excel\dfTemplate.xlsx")
    writer=pd.ExcelWriter(path,engine='xlsxwriter')
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

def UpdateIPs(path,WorkingWeeks):
    IPList=["PXIe Bottom10.92.6.46","HUBUDPXIE8880 TOP110.92.6.29"]
 
    xfile = openpyxl.load_workbook(path)

    sheet = xfile.get_sheet_by_name(WorkingWeeks[0])
    sheet['B1'] = IPList[0]
    xfile.save('text2.xlsx')
    xfile.close