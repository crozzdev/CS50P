import random
from typing import Generator

AMOUNT_MATH_PROBLEMS = 10


def main() -> None:
    score = 0
    level = get_level()

    for x, y in generate_math_problems(level):
        if ask_user_math_problem(x, y):
            score += 1

    print(f"Score: {score}")


def get_level() -> int:
    """Prompt until the user enters 1, 2, or 3; then return that level."""
    while True:
        try:
            level = int(input("Level: "))
            if level in (1, 2, 3):
                return level
        except ValueError:
            pass


def generate_integer(level: int) -> int:
    """Return a random non-negative integer with exactly `level` digits."""
    if level not in (1, 2, 3):
        raise ValueError

    low = 0 if level == 1 else 10 ** (level - 1)
    high = (10**level) - 1
    return random.randint(low, high)


def generate_math_problems(level: int) -> Generator[tuple[int, int], None, None]:
    """Yield AMOUNT_MATH_PROBLEMS pairs (x, y) for addition at the given level."""
    for _ in range(AMOUNT_MATH_PROBLEMS):
        yield generate_integer(level), generate_integer(level)


def ask_user_math_problem(x: int, y: int) -> bool:
    """Ask 'x + y = ' up to 3 times. On success return True; else show answer and return False."""
    attempts = 3
    while attempts:
        try:
            ans = int(input(f"{x} + {y} = "))
            if ans == x + y:
                return True
            print("EEE")
            attempts -= 1
        except ValueError:
            print("EEE")
            attempts -= 1

    print(f"{x} + {y} = {x + y}")
    return False


if __name__ == "__main__":
    main()
