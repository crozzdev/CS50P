def check_greeting(greeting: str) -> int:
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100


def main():
    greeting = input("Greeting: ").strip().lower()
    print(f"${check_greeting(greeting)}")


main()
