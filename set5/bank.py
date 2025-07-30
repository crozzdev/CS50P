def value(greeting: str) -> int:
    greeting = greeting.lower()
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20

    return 100


def main():
    greeting = input("Greeting: ")
    print(f"${value(greeting)}")


if __name__ == "__main__":
    main()
