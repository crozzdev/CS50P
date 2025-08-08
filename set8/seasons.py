import sys
from datetime import date

import inflect


def get_born_date(s) -> date:
    """Checks the user input and returns the input as a date object"""

    try:
        born_date = date.fromisoformat(s)
        if born_date > date.today():
            raise ValueError
        return born_date
    except ValueError:
        sys.exit("Invalid date")


def calculate_min_born(born_date: date) -> int:
    """Calculates the minutes since the born date until today"""
    today_date = date.today()
    delta_date = today_date - born_date

    return delta_date.days * 1440


def main():
    input_date = input("Enter your date of birth: ").strip()
    born_date = get_born_date(input_date)
    total_min = calculate_min_born(born_date)

    p = inflect.engine()
    print(f"{(p.number_to_words(total_min, andword='')).capitalize()} minutes")


if __name__ == "__main__":
    main()
