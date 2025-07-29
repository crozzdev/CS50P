import random


def prompt_positive_int(prompt: str) -> int:
    """Prompt until the user enters a positive integer (> 0)."""
    while True:
        try:
            n = int(input(f"{prompt} "))
            if n > 0:
                return n
        except ValueError:
            pass


def main() -> None:
    level = prompt_positive_int("Level:")
    target = random.randint(1, level)

    while True:
        guess = prompt_positive_int("Guess:")
        if guess < target:
            print("Too small!")
        elif guess > target:
            print("Too large!")
        else:
            print("Just right!")
            return


if __name__ == "__main__":
    main()
