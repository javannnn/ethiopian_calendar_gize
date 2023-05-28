import frappe
from datetime import date

ETHIOPIAN_MONTHS = {
    1: ("Meskerem", "September"),
    2: ("Tikimt", "October"),
    3: ("Hidar", "November"),
    4: ("Tahsas", "December"),
    5: ("Tir", "January"),
    6: ("Yekatit", "February"),
    7: ("Megabit", "March"),
    8: ("Miazia", "April"),
    9: ("Ginbot", "May"),
    10: ("Sene", "June"),
    11: ("Hamle", "July"),
    12: ("Nehase", "August"),
    13: ("Pagume", "Extra Month"),
}


@frappe.whitelist()
def get_ethiopian_date(gregorian_date=None):
    if not gregorian_date:
        frappe.throw("Gregorian date is required.")

    ethiopian_date = convert_to_ethiopian(gregorian_date)
    return {"ethiopian_date": ethiopian_date}


def convert_to_ethiopian(gregorian_date):
    gregorian_date = date.fromisoformat(gregorian_date)

    # Calculate the Ethiopian year
    ethiopian_year = (gregorian_date.year - 7) // 4

    # Calculate the Ethiopian month
    ethiopian_month = (gregorian_date.month - 9) % 13

    # Determine the number of days in the Ethiopian month
    days_in_month = 30 if ethiopian_month != 13 else 5 if is_leap_year(gregorian_date.year) else 6

    # Calculate the Ethiopian day
    ethiopian_day = gregorian_date.day if ethiopian_month != 13 else gregorian_date.day + 1

    # Get the names of the Ethiopian month and corresponding Gregorian month
    ethiopian_month_name, gregorian_month_name = ETHIOPIAN_MONTHS[ethiopian_month]

    # Format the Ethiopian date
    ethiopian_date = f"{ethiopian_year}/{ethiopian_month}/{ethiopian_day}"
    ethiopian_date += f" ({ethiopian_month_name} - {gregorian_month_name})"

    return ethiopian_date


def is_leap_year(year):
    # Check if the year is a leap year according to the Gregorian calendar rules
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

