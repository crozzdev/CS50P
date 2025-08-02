import csv
import sys


def check_arguments():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    if not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
        sys.exit("Not a CSV file.")


def get_scourgified(r_csv_path: str, w_csv_path: str) -> None:
    try:
        with open(r_csv_path, "r") as r_csv_file, open(w_csv_path, "a") as w_csv_file:
            csv_r_obj = csv.DictReader(r_csv_file)
            csv_w_obj = csv.DictWriter(
                w_csv_file, fieldnames=["first", "last", "house"]
            )
            csv_w_obj.writeheader()

            for row in csv_r_obj:
                last, first = row["name"].split(",")
                csv_w_obj.writerow(
                    {
                        "first": first.strip(),
                        "last": last,
                        "house": row["house"],
                    }
                )
    except FileNotFoundError:
        sys.exit(f"Could not read {r_csv_path}")


def main():
    check_arguments()
    get_scourgified(sys.argv[1], sys.argv[2])


if __name__ == "__main__":
    main()
