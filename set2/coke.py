COKE_COST = 50
COINS_ACCEPTED = [25, 10, 5]


def main():

    total_amount = 0

    while total_amount < COKE_COST:

        inserted_coin = int(input("Insert coin: "))

        if inserted_coin in COINS_ACCEPTED:
            total_amount += inserted_coin

        if total_amount < COKE_COST:
            print(f"Amount due: {COKE_COST - total_amount}")

    print(f"Change owed: {total_amount - COKE_COST}")


main()
