from model import Transaction
from services import TransactionService
from constants import OPTIONS, MODE_OPTIONS
from pydantic import ValidationError
from pyfiglet import Figlet
from datetime import datetime
from typing import Literal
import re


def get_title() -> str:
    """Gets the title of the transaction"""
    while True:
        title = input("Title:")
        if len(title) > 5:
            return title
        print("The title must be longer than 5 characters, please enter it again")


def get_description() -> str:
    """Gets the description of the transaction"""
    while True:
        description = input("Description: \n")
        if len(description) <= 255:
            return description
        print(
            "The description length cannot be longer than 255 characters, please enter it again"
        )


def get_date_from_user() -> datetime:
    """Gets a date from the user in various formats and returns a datetime object"""
    while True:
        date_str = input("Date (e.g. YYYY-MM-DD or MM/DD/YYYY): ")

        formats = [
            "%Y-%m-%d",  # 2025-12-08
            "%m/%d/%Y",  # 12/08/2025 (US style)
            "%d/%m/%Y",  # 08/12/2025 (Euro and Latin American style)
            "%Y/%m/%d",  # 2025/12/08
        ]

        for fmt in formats:
            try:
                return datetime.strptime(date_str, fmt)
            except ValueError:
                pass


def get_tags() -> list[str]:
    """Gets the tags of the transaction"""
    tags = input("Tags (comma separated): ")
    if tags:
        tags = re.sub(r"\s{2,}", " ", tags)
        return [tag.strip() for tag in tags.split(",")]
    return [""]


def get_amount() -> float:
    """Gets the amount of the transaction"""
    while True:
        try:
            amount = float(input("Amount ($): "))
            if amount > 0:
                return amount
            print("The amount must be greater than 0")
        except ValueError:
            print("The amount value is invalid, please enter it again")


def get_type_transaction() -> Literal["income", "expense"]:
    """Gets the type of the transaction (Income or Expense)"""
    while True:
        type_transaction = input("Type (Income/Expense): ").lower()
        if type_transaction in ["income", "expense"]:
            return "income" if type_transaction == "income" else "expense"
        print("Invalid transaction type, please enter 'Income' or 'Expense'")


def get_user_transaction() -> Transaction:
    """Gets the user transaction information from the terminal and outputs the corresponding Transaction object"""

    while True:
        try:
            title = get_title()
            description = get_description()
            date = get_date_from_user()
            tags = get_tags()
            amount = get_amount()
            type_transaction = get_type_transaction()

            transaction = Transaction(
                title=title,
                description=description,
                date=date,
                tags=tags,
                amount=amount,
                type_transaction=type_transaction,
            )
            return transaction

        except ValidationError as e:
            print("\nValidation errors:")
            for error in e.errors():
                field = error["loc"][0]
                message = error["msg"]
                print(f"  - {field}: {message}")


def get_mode_period() -> str:
    """Gets the mode of the transaction period filtering"""
    while True:
        mode = input(
            "\nSelect the mode for filtering by period (custom/month-year/year): "
        ).lower()
        if mode in MODE_OPTIONS:
            return mode
        print("You didn't choose a valid mode, please try again")


def get_key_dates(mode: str) -> list[str]:
    """Gets the key dates for filtering transactions by period based on the selected mode"""
    key_dates = []
    e_msg = "You entered the period in the wrong format, please try again"
    while True:
        try:
            if mode == "custom":
                date_input = input(
                    "Enter the date(s) for custom mode (YYYY-MM-DD). For a range, separate two dates with a comma: "
                )
                potential_dates = [d.strip() for d in date_input.split(",")]
                if not (1 <= len(potential_dates) <= 2):
                    e_msg = "You can only enter two dates: initial date and end date"
                    raise ValueError

                for d in potential_dates:
                    datetime.strptime(d, "%Y-%m-%d")
                key_dates = potential_dates
            elif mode == "month-year":
                month_year = input(
                    "Enter the month and year for month-year (YYYY-MM): "
                ).strip()
                datetime.strptime(month_year, "%Y-%m")
                key_dates.append(month_year)
            elif mode == "year":
                year = input("Enter the year (YYYY): ").strip()
                datetime.strptime(year, "%Y")
                key_dates.append(year)
            return key_dates
        except ValueError:
            print(e_msg)


def get_user_transaction_id(transactions: list[Transaction]) -> int:
    """Gets the transaction id the user wants to delete"""
    while True:
        try:
            transaction_id = int(
                input(
                    "Please enter the index(transaction id) of the transaction you want to delete"
                )
            )
            if 0 <= transaction_id < len(transactions):
                return transaction_id
            raise ValueError
        except ValueError:
            print(
                "The value is not valid either because is out of range or is not a number, please try again"
            )


def get_user_choice() -> int:
    """Displays the menu of options and get the user's choice"""
    while True:
        try:
            choice = int(
                input(
                    "\nWhat do you want to do? Please select a number\n1.Add a transaction\n2.Show all the transactions\n3.Show transactions by type\n4.Show transactions by period\nTo exit, press Ctrl+D or Ctrl+C\nChoice (only type a number): "
                )
            )
            if choice in OPTIONS:
                return choice
            raise ValueError
        except ValueError:
            print("You didn't chose a valid option, please enter it again")


def confirm_transaction_deletion(
    transaction_id: int, transactions: list[Transaction]
) -> bool | None:
    """Confirms to the user if they want to delete a certain transaction"""

    transaction_details = transactions[transaction_id]
    confirmation = input(
        f"Here is the details of the transaction you want to delete:\n{transaction_details}\nAre you sure you want to delete it? Please response (Y/N):\n"
    )
    if confirmation.lower() in ["y", "yes", "ok"]:
        return True
    print(
        "As you didn't confirm, the operation was cancelled and no transaction was deleted"
    )
    return False


def confirm_data_deletion() -> bool | None:
    """Confirms to the user if they want to delete all the transactions data"""

    confirmation = input(
        "Are you sure you want to delete ALL the transactions data? This action cannot be undone. Please respond DELETE (no other options are allowed):\n"
    )

    if confirmation.lower() == "delete":
        return True
    print("As you didn't confirm, the operation was cancelled and no data was deleted")
    return False


if __name__ == "__main__":
    f = Figlet(font="cybermedium", justify="center")
    print(f.renderText("Personal Finance CLI"))
    service = TransactionService()
    while True:
        try:
            choice = get_user_choice()
            match choice:
                case 1:
                    transaction = get_user_transaction()
                    service.add_transaction(transaction)
                    print("Transaction added sucessfully!")
                case 2:
                    service.show_transactions()
                case 3:
                    type_transaction = get_type_transaction()
                    service.show_transactions_by_type(type_transaction)
                case 4:
                    period_mode = get_mode_period()
                    key_dates = get_key_dates(period_mode)
                    service.show_transactions_by_period(period_mode, key_dates)
                case 5:
                    transaction_id = get_user_transaction_id(service.transactions)
                    if confirm_transaction_deletion(
                        transaction_id, service.transactions
                    ):
                        service.delete_transaction(transaction_id)
                case 6:
                    if confirm_data_deletion():
                        service.delete_data()
                        print("All transactions data deleted successfully.")
                case _:
                    print("You didn't choose a valid option, please try again")
        except (EOFError, KeyboardInterrupt):
            print("\nGoodBye! :)")
            break
