import datetime

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
