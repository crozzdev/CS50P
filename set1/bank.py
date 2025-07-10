def check_greeting(greeting: str) -> int:
    greeting = greeting.lower()
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100


def main():
    greeting = input("Greeting: ")
    print(f"${check_greeting(greeting)}")


main()
