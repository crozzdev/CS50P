from model import Transaction
from datetime import datetime
from tabulate import tabulate
import json


class TransactionService:
    def __init__(self, file_path: str = "finance.json"):
        self.file_path = file_path
        self.transactions: list[Transaction] = []
        self.load_data()

    def _dump_transactions(self) -> list[dict]:
        return [t.model_dump(mode="json") for t in self.transactions]

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
            print("No file found or invalid JSON, creating a new one")
            self.transactions = []

    def add_transaction(self, transaction: Transaction) -> None:
        self.transactions.append(transaction)
        self.save_data()

    def show_transactions(self) -> None:
        data = self._dump_transactions()
        print(tabulate(data, headers="keys"))

    def calculate_balance(self) -> float:
        balance = 0
        if not self.transactions:
            return balance
        for t in self.transactions:
            if t.type_transaction == "income":
                balance += t.amount
            else:
                balance -= t.amount
        return balance


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
    print(service.calculate_balance())
    service.show_transactions()
