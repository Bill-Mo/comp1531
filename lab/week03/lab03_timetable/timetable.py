from datetime import date, time, datetime

def timetable(dates, times):
    '''
    Generates a list of datetimes given a list of dates and a list of times. All possible combinations of date and time are contained within the result. The result is sorted in chronological order.

    For example,
    >>> timetable([date(2019,9,27), date(2019,9,30)], [time(14,10), time(10,30)])
    [datetime(2019,9,27,10,30), datetime(2019,9,27,14,10), datetime(2019,9,30,10,30), datetime(2019,9,30,14,10)]
    '''
    #if dates[0] < dates[1]:
      #  print(dates[1])
    #day = datetime(dates[0].year, dates[0].month, dates[0].day, times[0].hour, times[0].minute)
    ordered_date = {}
    for i in dates:
        order = 0
        for j in dates:
            if i > j:
                order += 1
        ordered_date[order] = i
        
    ordered_time = {}
    for i in times:
        order = 0
        for j in times:
            if i > j:
                order += 1
        ordered_time[order] = i
        
    all_date = []
    for i in range(len(ordered_date)):
        for j in range(len(ordered_time)):
            day = datetime(ordered_date[i].year, ordered_date[i].month, ordered_date[i].day, ordered_time[j].hour, ordered_time[j].minute)
            all_date.append(day)
    print(all_date) 
    return all_date
        
timetable([date(2019,9,27), date(2019,9,30)], [time(14,10), time(10,30)])

