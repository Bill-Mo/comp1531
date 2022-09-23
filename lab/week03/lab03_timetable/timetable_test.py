from datetime import date, time, datetime
from timetable import timetable
import pytest

def test_example():
    assert timetable([date(2019,9,27), date(2019,9,30)], [time(14,10), time(10,30)]) == [datetime(2019,9,27,10,30), datetime(2019,9,27,14,10), datetime(2019,9,30,10,30), datetime(2019,9,30,14,10)]
    
def test_ordered():
    assert timetable([date(2020, 2, 25), date(2020, 5, 15), date(2020, 8, 2)], [time(7, 10), time(10, 25)]) == [datetime(2020, 2, 25, 7, 10), datetime(2020, 2, 25, 10, 25), datetime(2020, 5, 15, 7, 10), datetime(2020, 5, 15, 10, 25), datetime(2020, 8, 2, 7, 10), datetime(2020, 8, 2, 10, 25)]
