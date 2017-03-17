from datetime import date


def days_until_christmas(day):
    year = day.year
    if day >= date(year, 12, 26):
        year += 1
    return (date(year, 12, 25) - day).days
