import re

HOUR_MAP = {
    "12 AM": "00",
    "1 AM": "01",
    "2 AM": "02",
    "3 AM": "03",
    "4 AM": "04",
    "5 AM": "05",
    "6 AM": "06",
    "7 AM": "07",
    "8 AM": "08",
    "9 AM": "09",
    "10 AM": "10",
    "11 AM": "11",
    "12 PM": "12",
    "1 PM": "13",
    "2 PM": "14",
    "3 PM": "15",
    "4 PM": "16",
    "5 PM": "17",
    "6 PM": "18",
    "7 PM": "19",
    "8 PM": "20",
    "9 PM": "21",
    "10 PM": "22",
    "11 PM": "23",
}


def main():
    print(convert(input("Hours: ")))


def convert(s: str) -> str:
    sub_pattern_f_hour = r"(?P<first_hour>[1-9]|10|11|12)(?::(?P<first_hour_minutes>[0-5][0-9]))? (?P<first_hour_ampm>AM|PM)"

    sub_pattern_s_hour = r"(?P<second_hour>[1-9]|10|11|12)(?::(?P<second_hour_minutes>[0-5][0-9]))? (?P<second_hour_hour_ampm>AM|PM)"

    pattern = f"^{sub_pattern_f_hour} to {sub_pattern_s_hour}$"
    if matches := re.search(pattern, s):
        first_hour = matches.group("first_hour")
        first_hour_minutes = matches.group("first_hour_minutes")
        first_hour_ampm = matches.group("first_hour_ampm")
        second_hour = matches.group("second_hour")
        second_hour_minutes = matches.group("second_hour_minutes")
        second_hour_ampm = matches.group("second_hour_hour_ampm")

        first_hour_24f = (
            f"{HOUR_MAP[f'{first_hour} {first_hour_ampm}']}:{first_hour_minutes}"
            if first_hour_minutes
            else f"{HOUR_MAP[f'{first_hour} {first_hour_ampm}']}:00"
        )
        second_hour_24f = (
            f"{HOUR_MAP[f'{second_hour} {second_hour_ampm}']}:{second_hour_minutes}"
            if second_hour_minutes
            else f"{HOUR_MAP[f'{second_hour} {second_hour_ampm}']}:00"
        )

        return f"{first_hour_24f} to {second_hour_24f}"
    raise ValueError


if __name__ == "__main__":
    main()
