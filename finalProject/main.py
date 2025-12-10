from model import Transaction
from services import TransactionService
from pydantic import ValidationError
from pyfiglet import Figlet
from datetime import datetime
from typing import Literal
import re

OPTIONS = [1, 2, 3]


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


def get_user_choice() -> int:
    """Displays the menu of options and get the user's choice"""
    while True:
        try:
            choice = int(
                input(
                    "\nWhat do you want to do? Please select a number\n1.Add a transaction\n2.Show all the transactions\n3.Show transactions by type\n"
                )
            )
            if choice in OPTIONS:
                return choice
            raise ValueError
        except ValueError:
            print("You didn't chose a valid option, please enter it again")


if __name__ == "__main__":
    f = Figlet(font="cybermedium", justify="center")
    print(f.renderText("Personal Finance CLI"))
    service = TransactionService()
    while True:
        try:
            choice = get_user_choice()
            if choice == 1:
                transaction = get_user_transaction()
                service.add_transaction(transaction)
                print("Transaction added sucessfully!")
            elif choice == 2:
                service.show_transactions()
            elif choice == 3:
                type_transaction = get_type_transaction()
                service.show_transactions_by_type(type_transaction)
        except (EOFError, KeyboardInterrupt):
            print("\nGoodBye! :)")
            break
