import sys

MONTHS = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12,
}

MAX_DAYS_MONTH = 31
MAX_MONTHS_YEAR = 12


def get_and_check_date() -> list:

    while True:

        try:
            date_str = input("Date: ").strip()
            if "/" not in date_str and "," not in date_str:
                continue
            date_list = date_str.split() if not "/" in date_str else date_str.split("/")
            if len(date_list) == 3:
                month, day, year = date_list

                day = day.replace(",", "")

                is_valid_day = day.isdigit() and 0 < int(day) <= MAX_DAYS_MONTH
                is_valid_year = year.isdigit() and len(year) <= 4

                if (
                    is_valid_day
                    and is_valid_year
                    and month.isalpha()
                    and month in MONTHS.keys()
                ):
                    month = MONTHS[month]
                    return [int(year), int(month), int(day)]
                if (
                    is_valid_day
                    and is_valid_year
                    and month.isdigit()
                    and 0 < int(month) <= MAX_MONTHS_YEAR
                ):
                    return [int(year), int(month), int(day)]

        except EOFError:
            sys.exit(0)


def main():
    date = get_and_check_date()
    year, month, day = date
    print(f"{year}-{month:02}-{day:02}")


main()
