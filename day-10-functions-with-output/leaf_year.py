def is_leap_year(year):
    b = False
    if year % 4 == 0:
        b = True
    if year % 100 == 0:
        b = False
    if year % 400 == 0:
        b = True
    return b