import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    """
    Check if the IP is a valid ip address, the pattern is as follows:

    - `^` and `$`: Match the start and end of the string (ensures the whole input is validated).
    - `(?: ... )`: Non-capturing group, used for grouping without capturing.
    - `25[0-5]`: Matches 250–255.
    - `2[0-4][0-9]`: Matches 200–249.
    - `1[0-9]{2}`: Matches 100–199.
    - `[1-9]?[0-9]`: Matches 0–99 (optional leading digit for 1–9, then 0–9).
    - The first group matches the first octet.
    - `(?:.(...)){3}`: The same pattern, preceded by a dot, repeated three times for the remaining octets.

    """
    pattern = r"^(?:25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])(?:\.(?:25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])){3}$"

    if re.search(pattern, ip):
        return True

    return False


if __name__ == "__main__":
    main()
