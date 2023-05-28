from ethiopian_date import EthiopianDate
def convert_to_ethiopian_date(gregorian_date):
    ethiopian_date = EthiopianDate.from_gregorian(year=gregorian_date.year, month=gregorian_date.month, day=gregorian_date.day)
    return ethiopian_date

