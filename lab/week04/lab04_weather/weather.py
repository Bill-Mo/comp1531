import datetime
import csv

def weather(date, location):
    with open('weatherAUS.csv') as f:
        min_avg = 0
        max_avg = 0
        the_min = 0
        the_max = 0
        how_many_days = 0
        is_day_exist = 0
        l = date.split('-', 3)
        l.reverse()
        rdate = '-'.join(l)
        data = csv.reader(f)
        for day in data:
            if location == day[1]:
                if rdate == day[0]:
                    if day[2] == 'NA' or day[3] == 'NA':
                        return (None, None)
                    the_min = float(day[2])
                    the_max = float(day[3])
                    is_day_exist = 1
                if day[2] != 'NA' and day[3] != 'NA':
                    min_avg += float(day[2])
                    max_avg += float(day[3])
                    how_many_days += 1
        if how_many_days == 0 or is_day_exist == 0:
            return (None, None)
        min_avg = min_avg / how_many_days
        max_avg = max_avg / how_many_days
        #print('min_avg: ', min_avg, 'max_avg: ', max_avg, 'days: ', how_many_days, 'the_min: ', the_min, 'the_max: ', the_max)
        return (round((min_avg - the_min), 1), round((the_max - max_avg), 1))
        

