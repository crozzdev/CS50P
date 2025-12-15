from model import Transaction
from datetime import datetime
from tabulate import tabulate
from typing import Literal
import os
import json


class TransactionService:
    def __init__(self, file_path: str = "finance.json"):
        self.file_path = file_path
        self.transactions: list[Transaction] = []
        self.load_data()

    def _dump_transactions(self) -> list[dict]:
        return [t.model_dump(mode="json") for t in self.transactions]

    def _show_totals(self, totals: tuple[float, float, float]) -> None:
        total_income, total_expense, balance = totals
        print(f"Total income: ${total_income}")
        print(f"Total Expense: ${total_expense}")
        print(f"Balance: ${balance}\n")

    def save_data(self) -> None:
        with open(self.file_path, "w") as json_file:
            data = self._dump_transactions()
            json.dump(data, json_file, indent=2)

    def load_data(self) -> None:
        try:
            with open(self.file_path, "r") as json_file:
                data = json.load(json_file)
                self.transactions = [Transaction(**t) for t in data]
        except (FileNotFoundError, json.JSONDecodeError):
            print("No file found or invalid JSON, creating a new one\n")
            self.transactions = []

    def delete_data(self) -> None:
        """Deletes all the transactions data"""
        try:
            os.remove(self.file_path)
            self.transactions = []
        except FileNotFoundError:
            print("No file found to delete\n")

    def add_transaction(self, transaction: Transaction) -> None:
        self.transactions.append(transaction)
        self.organize_transactions()
        self.save_data()

    def show_transactions(self) -> None:
        data = self._dump_transactions()

        print(tabulate(data, headers="keys", tablefmt="fancy_grid", showindex=True))
        self._show_totals(self.get_totals())

    def show_transactions_by_type(
        self, type_transaction: Literal["income", "expense"]
    ) -> None:
        data = list(
            filter(
                lambda t: t.get("type_transaction") == type_transaction,
                self._dump_transactions(),
            )
        )

        if data:
            total = sum([t.get("amount", 0) for t in data])

            print(tabulate(data, headers="keys", tablefmt="grid", showindex=True))
            print(f"Total: {total}\n")
        else:
            print(f"No transactions found with the type: {type_transaction}")

    def get_totals(
        self, transactions: list[Transaction] = []
    ) -> tuple[float, float, float]:
        """Returns the total income, expense and balance for the specified group of transactions"""
        total_income = 0
        total_expense = 0
        balance = 0

        if not transactions:
            transactions = self.transactions

        total_income = sum(
            [t.amount for t in transactions if t.type_transaction == "income"]
        )
        total_expense = sum(
            [t.amount for t in transactions if t.type_transaction == "expense"]
        )
        balance = total_income - total_expense

        return (total_income, total_expense, balance)

    def organize_transactions(self, order: bool = True) -> None:
        """Organizes the transactions in chronological order either ascending (older first) or descending(newer first)"""
        self.transactions = sorted(
            self.transactions, key=lambda t: t.date, reverse=order
        )

    def show_transactions_by_period(self, mode: str, key_dates: list[str]) -> None:
        """Show transactions by date based on the specified mode and key_dates"""
        grouped_transactions = []

        for transaction in self.transactions:
            if mode == "custom":
                date_key = transaction.date.strftime("%Y-%m-%d")
            elif mode == "month-year":
                date_key = transaction.year_month_key
            else:
                date_key = str(transaction.year)

            if date_key in key_dates:
                grouped_transactions.append(transaction)

        if not grouped_transactions:
            print("No transactions found for the specified period.")
            return None

        print(
            tabulate(
                [t.model_dump(mode="json") for t in grouped_transactions],
                headers="keys",
                tablefmt="fancy_grid",
                showindex=True,
            )
        )
        self._show_totals(self.get_totals(grouped_transactions))

    def delete_transaction(self, transaction_id: int) -> None:
        """Deletes the transaction at specified index"""
        try:
            self.transactions.pop(transaction_id)
            print(f"Transaction ID {transaction_id} deleted successfully.")
            self.save_data()
        except IndexError:
            print(f"Transaction ID {transaction_id} is out of range.")


if __name__ == "__main__":
    service = TransactionService()
    service.add_transaction(
        Transaction(
            title="Salary",
            description="Monthly salary",
            date=datetime(2023, 10, 1),
            tags=["work"],
            amount=5000.0,
            type_transaction="income",
        )
    )
    service.add_transaction(
        Transaction(
            title="Groceries",
            description="Weekly groceries",
            date=datetime(2023, 10, 2),
            tags=None,
            amount=100.0,
            type_transaction="expense",
        )
    )
    print(service.get_totals())
    service.show_transactions()
    service.show_transactions_by_type("income")
    service.show_transactions_by_type("expense")
    service.delete_transaction(0)
    service.show_transactions_by_type("expense")
    service.show_transactions()
