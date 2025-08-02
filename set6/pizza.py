import csv
import sys

from tabulate import tabulate


def check_arguments():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")


def get_csv_rows(path: str) -> list[list[str]]:
    try:
        csv_r_list = []
        with open(path, "r") as csv_file:
            csv_r = csv.reader(csv_file)
            for row in csv_r:
                csv_r_list.append(row)

        return csv_r_list
    except FileNotFoundError:
        sys.exit("CSV file does not exist")


def main():
    check_arguments()
    csv_r_list = get_csv_rows(sys.argv[1])
    print(tabulate(csv_r_list, headers="firstrow", tablefmt="grid"))


if __name__ == "__main__":
    main()
