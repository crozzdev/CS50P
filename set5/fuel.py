def main():
    while True:
        try:
            fraction = input("Fraction: ")
            percentage = convert(fraction)
            gauge_str = gauge(percentage)
            break
        except ValueError:
            pass
        except ZeroDivisionError:
            pass
    print(gauge_str)


def convert(fraction: str) -> int:
    x, y = fraction.split("/")

    int_x, int_y = int(x), int(y)
    if int_y == 0:
        raise ZeroDivisionError
    if (int_x > int_y) or (int_x < 0 or int_y < 0):
        raise ValueError

    return round((int_x / int_y) * 100)


def gauge(percentage: int) -> str:
    if percentage <= 1:
        return "E"
    if percentage >= 99:
        return "F"
    return f"{percentage}%"


if __name__ == "__main__":
    main()
