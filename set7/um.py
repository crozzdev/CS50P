import re


def main():
    print(count(input("Text: ")))


def count(s):
    """Counts how many 'ums' there are in a given string (s)"""

    pattern = r"\bum\b"

    return len(re.findall(pattern, s, re.IGNORECASE))


if __name__ == "__main__":
    main()
