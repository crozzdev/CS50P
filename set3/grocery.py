def build_grocery_dict() -> dict[str, int]:
    grocery_dict = {}
    while True:
        try:
            item = input()
        except EOFError:
            print("")
            return grocery_dict

        grocery_dict[item] = grocery_dict.get(item, 0) + 1


def main():
    grocery_dict = build_grocery_dict()
    for item in sorted(grocery_dict):
        print(grocery_dict[item], end=" ")
        print(item.upper())


main()
