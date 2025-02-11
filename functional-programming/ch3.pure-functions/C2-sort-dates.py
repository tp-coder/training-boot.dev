# Fix the sort_dates function. It takes as input a list of dates in "MONTH-DAY-YEAR" format 
# and returns a list of the dates sorted in ascending order.

def sort_dates(dates):
    return sorted(dates, key=rearrange_dates)

# helper function to arrange the dates in a way that sorted compares YEAR - MONTH - DAY
def rearrange_dates(date_string):
    month, day, year = date_string.split("-")
    return year + month + day