days = ["Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday", "Sunday"]

odd_days = {
    0: 0,
    100: 5,
    200: 3,
    300: 1
}

month_odd_days = {
    1: 3,
    2: [0, 1],
    3: 3,
    4: 2,
    5: 3,
    6: 2,
    7: 3,
    8: 3,
    9: 2,
    10: 3,
    11: 2,
    12: 1
}


def find_day(date):
    date_splitted = date.split("-")
    day = int(date_splitted[0])
    month = int(date_splitted[1])
    year = int(date_splitted[2])
    if day > 31:
        return "invalid date"
    elif month > 12:
        return "invalid month"
    elif year < 0:
        return "invalid year"
    odd_days_of_year = odd_days_year(year)
    if year % 400 == 0:
        leap_year = True
    elif year % 100 != 0 and year % 4 == 0:
        leap_year = True
    else:
        leap_year = False
    odd_days_daynmonth = odd_days_of_day_and_month(
        day, month, leap_year)
    total_odd_days = odd_days_of_year + odd_days_daynmonth
    return days[total_odd_days % 7 - 1]


def odd_days_year(year):
    years_completed = year - 1
    new_year = years_completed % 400
    century_year = (new_year // 100)*100
    remaining_year = new_year % 100

    for k, v in odd_days.items():
        if century_year == k:
            odd_days_century_year = v

    leap_year_in_remaining_year = remaining_year // 4
    ordinary_year_in_remaining_year = remaining_year - leap_year_in_remaining_year
    odd_days_in_leap_year = leap_year_in_remaining_year * 2
    odd_days_in_ordinary_year = ordinary_year_in_remaining_year * 1
    total_odd_days = odd_days_century_year + \
        odd_days_in_leap_year + odd_days_in_ordinary_year
    return total_odd_days % 7


def odd_days_of_day_and_month(day, month, leap_year):
    odd_days_of_month = 0
    for k, v in month_odd_days.items():
        if k == 2:
            if leap_year:
                v = month_odd_days[2][1]
            else:
                v = month_odd_days[2][0]
        elif k == month:
            break
        else:
            odd_days_of_month += v
            continue
    total_odd_days = odd_days_of_month + day
    return total_odd_days % 7


print(find_day("17-01-2006"))
