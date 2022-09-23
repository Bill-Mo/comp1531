import sys

def pretty_date(time):
    time_one = time[0:2]
    time_two = time[2:-1]
    sufix = ''
    time = int(time)
    if time > 1200:
        sufix = ' PM'
        if time > 1300:
            time -= 1200
    else:
        sufix = ' AM'
    time = time_one + ':' + time_two + sufix
    return time

l = []
for line in sys.stdin:
    l.append(pretty_date(line))
for line in l:
    print(line)
