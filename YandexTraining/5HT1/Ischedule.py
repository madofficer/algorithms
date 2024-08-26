MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
          'December']
DAYS_OF_WEEK = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
DAYS = [[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31], [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]]


def leap_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return DAYS[1]
    else:
        return DAYS[0]


def get_day_of_week(year, month, day, start_day):
    days_gone = sum(leap_year(year)[:MONTHS.index(month)]) + day
    return DAYS_OF_WEEK[(days_gone - 1 + DAYS_OF_WEEK.index(start_day)) % 7]


n = int(input())

year = int(input())

holidays = {x: [] for x in MONTHS}
days_in_year = {x: 0 for x in DAYS_OF_WEEK}

for _ in range(n):
    d, m = input().split()
    holidays[m].append(int(d))

day_of_week = input()

for i in range(sum(leap_year(year))):
    days_in_year[DAYS_OF_WEEK[(DAYS_OF_WEEK.index(day_of_week) + i) % 7]] += 1

for month, days in holidays.items():
    for day in days:
        days_in_year[get_day_of_week(year, month, day, day_of_week)] -= 1

print(max(days_in_year, key=days_in_year.get), min(days_in_year, key=days_in_year.get))
