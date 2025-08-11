def main():
    time = input("What time is it?: ")
    time_float = convert(time)
    if 7.00 <= time_float <= 8.00:
        print("breakfast time")
    elif 12.00 <= time_float <= 13.00:
        print("lunch time")
    elif 18.00 <= time_float <= 19.00:
        print("dinner time")
    else:
        print("")


def convert(time: str) -> float:
    """Convert time in HH:MM format to float representation (HH.MM)."""
    if not time:
        return 0.0

    hours, minutes = time.split(":")
    return float(hours) + (float(minutes) / 60.0)


if __name__ == "__main__":
    main()
