def main():
    percentage = get_percentage()
    print(percentage)


def get_percentage() -> str:
    percentage = ""
    while True:
        fraction = input("Fraction: ")

        try:
            x, y = fraction.split("/")
            int_x, int_y = int(x), int(y)
            if (int_x > int_y) or (int_x < 0 or int_y < 0):
                raise ValueError
            if int_x / int_y >= 0.99:
                percentage = "F"
            elif int_x / int_y <= 0.01:
                percentage = "E"
            else:
                percentage = f"{round((int_x / int_y) * 100)}%"

        except ZeroDivisionError:
            pass
        except ValueError:
            pass
        else:
            return percentage


main()
