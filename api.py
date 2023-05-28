import frappe
from datetime import date
from ethiopian_date import EthiopianDateConverter

@frappe.whitelist()
def get_ethiopian_date(gregorian_date=None):
    if not gregorian_date:
        frappe.throw("Gregorian date is required.")

    year, month, day = map(int, gregorian_date.split("-"))
    ethiopian_date = EthiopianDateConverter.to_ethiopian(year, month, day)

    ethiopian_year = ethiopian_date.year
    ethiopian_month = ethiopian_date.month
    ethiopian_day = ethiopian_date.day

    ethiopian_date_str = f"{ethiopian_day:02d}/{ethiopian_month:02d}/{ethiopian_year}"

    return {"ethiopian_date": ethiopian_date_str}

