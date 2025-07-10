def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d: str) -> float:
    "Convert the input which is expected to be in the format $xx.xx into the float representation"

    d = d.replace("$", "")
    return float(d) / 100


def percent_to_float(p: str) -> float:
    "Convert the input which is expected to be in the format xx% into the float representation"
    p = p.replace("%", "")
    return float(p)


main()
