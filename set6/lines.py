import sys


def check_argument():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    if not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file.")


def get_file_content() -> int:
    check_argument()
    file_path = sys.argv[1]
    count = 0

    try:
        with open(file_path, "r") as file:
            for line in file:
                s_line = line.strip()
                if not s_line or s_line.startswith("#"):
                    continue
                count += 1
        return count
    except FileNotFoundError:
        sys.exit("File does not exist")


def main():
    count = get_file_content()
    print(count)


if __name__ == "__main__":
    main()
