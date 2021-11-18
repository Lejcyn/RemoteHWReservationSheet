import datetime

def workdays(d, end, excluded=(6, 7)):
    days = []
    while d.date() <= end.date():
        if d.isoweekday() not in excluded:
            days.append(d)
        d += datetime.timedelta(days=1)
    return days

TotalDays=workdays(datetime.datetime(2021, 1, 1),datetime.datetime(2021, 12, 31))


Data = TotalDays[22]
print(Data.day,"\t",Data.month)

WW=Data.isocalendar()[1]
LastElem=TotalDays[len(TotalDays)-1]
TotalWeeks=[[]for i in range(LastElem.isocalendar()[1])]
for data in TotalDays:
    TotalWeeks[data.isocalendar()[1]-1].append(data)
print(TotalWeeks)