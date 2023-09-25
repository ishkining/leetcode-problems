def days_and_seconds(year1, month1, day1, hour1, min1, sec1,
                     year2, month2, day2, hour2, min2, sec2):
    days = 0

    while year1 != year2 or month1 != month2 or day1 != day2:
        days += 1

        day1 += 1

        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if day1 > days_in_month[month1 - 1]:
            day1 = 1
            month1 += 1

        if month1 > 12:
            month1 = 1
            year1 += 1

    seconds = (hour2 * 3600 + min2 * 60 + sec2) - (hour1 * 3600 + min1 * 60 + sec1)

    if seconds < 0:
        seconds = 86400 - abs(seconds)
        days -= 1

    return days, seconds


y1, m1, d1, h1, min1, sec1 = map(int, input().split())
y2, m2, d2, h2, min2, sec2 = map(int, input().split())

result = days_and_seconds(y1, m1, d1, h1, min1, sec1, y2, m2, d2, h2, min2, sec2)
print(*result)