from calendar import TextCalendar


def get_month_calendar(month: int, year: int) -> list:
    cl = TextCalendar()
    month = cl.monthdays2calendar(year, month)
    return month
