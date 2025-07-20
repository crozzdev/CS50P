MONTHS = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


def parse_numeric_date(date_str):
    """Parse MM/DD/YYYY format"""
    try:
        parts = date_str.split("/")
        if len(parts) != 3:
            return None

        month_str, day_str, year_str = parts
        month = int(month_str)
        day = int(day_str)
        year = int(year_str)

        # Validate ranges
        if not (1 <= month <= 12 and 1 <= day <= 31):
            return None

        return year, month, day
    except ValueError:
        return None


def parse_textual_date(date_str):
    """Parse 'Month DD, YYYY' format"""
    try:
        # Remove comma and split by spaces
        date_str = date_str.replace(",", "")
        parts = date_str.split()

        if len(parts) != 3:
            return None

        month_str, day_str, year_str = parts

        # Check if month is valid
        if month_str not in MONTHS:
            return None

        month = MONTHS.index(month_str) + 1
        day = int(day_str)
        year = int(year_str)

        # Validate ranges
        if not (1 <= day <= 31):
            return None

        return year, month, day
    except ValueError:
        return None


def get_date():
    """Prompt user for date until valid input is provided"""
    while True:
        date_input = input("Date: ").strip()

        # Try parsing as numeric format first
        if "/" in date_input:
            result = parse_numeric_date(date_input)
            if result:
                return result

        # Try parsing as textual format
        elif "," in date_input:
            result = parse_textual_date(date_input)
            if result:
                return result

        # If neither format works, continue the loop (reprompt)
        continue


def main():
    year, month, day = get_date()
    print(f"{year}-{month:02d}-{day:02d}")


if __name__ == "__main__":
    main()
