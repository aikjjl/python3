from datetime import datetime

def get_person(n, y, r):
    day = datetime.date.today()
    persons_on_duty = ['raymondzhu', 'yakovliu', 'shabbywu', 'bluesyu']
    while day < datetime.date(n, y, r):
        year, week, day_of_the_week = day.isocalendar()
        trans = week % len(persons_on_duty)
        person = persons_on_duty[trans]
        day += datetime.timedelta(days=7)
        print(u"%s年第%s周：值班人%s" % (year, week, person))

# get_person(2020,08,24)
get_person(2020,7,24)