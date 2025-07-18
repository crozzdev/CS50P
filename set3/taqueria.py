MENU = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00,
}


def main():

    order = []
    while True:
        try:
            item = input("Item: ")
            item_value = MENU[item.lower().title()]
        except EOFError:
            print("\n")
            return
        except KeyError:
            pass
        else:
            order.append(item_value)
            print(f"Total: ${sum(order):.2f}")


main()
