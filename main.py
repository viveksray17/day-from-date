from data import days, month_odd_days, century_odd_days


def find_day(day, month, year):
    # Restrictions
    if day > 31:
        return "invalid date"
    elif month > 12:
        return "invalid month"
    elif year <= 0:
        return "invalid year"
    else:
        # Odd days in year calculation
        years_completed = year - 1
        new_year = years_completed % 400
        century_year = (new_year // 100)*100
        remaining_year = new_year - century_year

        # Odd days for century
        for k, v in century_odd_days.items():
            if century_year == k:
                odd_days_century_year = v

        # Leap and non-leap year calculation
        leap_year_in_remaining_year = remaining_year // 4
        ordinary_year_in_remaining_year = remaining_year - leap_year_in_remaining_year

        # Odd days in leap and non-leap year
        odd_days_in_leap_year = leap_year_in_remaining_year * 2
        odd_days_in_ordinary_year = ordinary_year_in_remaining_year * 1

        # Total odd days of year and non-leap year
        total_odd_days_of_year = odd_days_century_year + \
            odd_days_in_leap_year + odd_days_in_ordinary_year

        # Odd days in day and month calculation
        # Check if leap year
        if year % 400 == 0:
            leap_year = True
        elif year % 100 != 0 and year % 4 == 0:
            leap_year = True
        else:
            leap_year = False
        odd_days_of_month = 0

        # Odd days in month
        for k, v in month_odd_days.items():
            # If the key is equal to the month we don't need to add the odd days
            if k == month:
                break

            else:
                if k == 2:
                    # If it is a leap year then February has 1 odd day otherwise 0
                    if leap_year:
                        v = month_odd_days[2][1]
                    else:
                        v = month_odd_days[2][0]
                odd_days_of_month += v
        total_odd_days_of_month_and_day = odd_days_of_month + day

        # Final result
        final_odd_days = (total_odd_days_of_year +
                          total_odd_days_of_month_and_day) % 7
        return days[final_odd_days - 1]


if __name__ == "__main__":
    print(find_day(12, 12, 2012))
