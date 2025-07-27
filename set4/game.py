import random


def get_positive_int_input(message: str) -> int:
    """Prompt until a positive integer (n>0) is provided"""
    num = 0
    while num <= 0:
        try:
            num = int(input(f"{message} "))
        except ValueError:
            pass
    return num


def main():
    level = get_positive_int_input("Level:")

    target = random.randint(1, level)

    while True:
        guess = get_positive_int_input("Guess:")

        if guess < target:
            print("Too small!")
        elif guess > target:
            print("Too large!")
        else:
            print("Just right!")
            break


main()
