import inflect

ADIEU_STR_PREFIX = "Adieu, adieu, to "


def main():
    names_list = []
    p = inflect.engine()

    while True:
        try:
            name = input("Name: ")
            names_list.append(name)
        except EOFError:
            print()
            break

    print(ADIEU_STR_PREFIX + p.join(names_list))


main()
