import pytest
import json
import tempfile
import os
from datetime import datetime
from model import Transaction
from services import TransactionService


@pytest.fixture
def temp_file():
    # Create a temporary file for testing
    with tempfile.NamedTemporaryFile(mode="w+", delete=False, suffix=".json") as f:
        yield f.name
    # Cleanup after test
    os.unlink(f.name)


@pytest.fixture
def sample_transactions():
    return [
        Transaction(
            title="Salary",
            description="Monthly salary",
            date=datetime(2023, 10, 1),
            tags=["work"],
            amount=5000.0,
            type_transaction="income",
        ),
        Transaction(
            title="Groceries",
            description="Weekly groceries",
            date=datetime(2023, 10, 2),
            tags=None,
            amount=100.0,
            type_transaction="expense",
        ),
    ]


def test_init_with_no_file(temp_file):
    # Test initialization when file doesn't exist
    service = TransactionService(temp_file)
    assert service.transactions == []
    assert service.file_path == temp_file


def test_init_with_existing_file(temp_file, sample_transactions):
    # Test initialization with existing file
    data = [t.model_dump(mode="json") for t in sample_transactions]
    with open(temp_file, "w") as f:
        json.dump(data, f)

    service = TransactionService(temp_file)
    assert len(service.transactions) == 2
    assert service.transactions[0].title == "Salary"
    assert service.transactions[1].title == "Groceries"


def test_save_data(temp_file, sample_transactions):
    # Test saving data to file
    service = TransactionService(temp_file)
    service.transactions = sample_transactions
    service.save_data()

    with open(temp_file, "r") as f:
        data = json.load(f)

    assert len(data) == 2
    assert data[0]["title"] == "Salary"
    assert data[1]["title"] == "Groceries"


def test_load_data(temp_file, sample_transactions):
    # Test loading data from file
    data = [t.model_dump(mode="json") for t in sample_transactions]
    with open(temp_file, "w") as f:
        json.dump(data, f)

    service = TransactionService(temp_file)
    service.load_data()

    assert len(service.transactions) == 2
    assert service.transactions[0].title == "Salary"
    assert service.transactions[1].title == "Groceries"


def test_add_transaction(temp_file):
    # Test adding a transaction
    service = TransactionService(temp_file)
    transaction = Transaction(
        title="Test1",
        description="Test transaction",
        date=datetime(2023, 10, 3),
        tags=None,
        amount=200.0,
        type_transaction="expense",
    )
    service.add_transaction(transaction)

    assert len(service.transactions) == 1
    assert service.transactions[0].title == "Test1"

    # Check if saved to file
    with open(temp_file, "r") as f:
        data = json.load(f)
    assert len(data) == 1
    assert data[0]["title"] == "Test1"


def test_calculate_totals_empty(temp_file):
    # Test balance with no transactions
    service = TransactionService(temp_file)
    assert service.get_totals() == (0.0, 0.0, 0.0)


def test_calculate_totals_with_transactions(sample_transactions):
    service = TransactionService()
    service.transactions = sample_transactions

    assert service.get_totals() == (5000.0, 100.0, 4900.0)


def test_calculate_totals_multiple_transactions():
    # Test with more transactions
    service = TransactionService()
    service.transactions = [
        Transaction(
            title="Income1",
            description="",
            date=datetime(2023, 10, 1),
            tags=None,
            amount=1000.0,
            type_transaction="income",
        ),
        Transaction(
            title="Expense1",
            description="",
            date=datetime(2023, 10, 2),
            tags=None,
            amount=200.0,
            type_transaction="expense",
        ),
        Transaction(
            title="Income2",
            description="",
            date=datetime(2023, 10, 3),
            tags=None,
            amount=500.0,
            type_transaction="income",
        ),
        Transaction(
            title="Expense2",
            description="",
            date=datetime(2023, 10, 4),
            tags=None,
            amount=100.0,
            type_transaction="expense",
        ),
    ]
    # 1000 + 500 - 200 - 100 = 1200
    assert service.get_totals() == (1500.0, 300.0, 1200.0)


def test_show_transactions_empty(capfd, temp_file):
    # Test showing transactions when list is empty
    service = TransactionService(temp_file)
    service.show_transactions()
    captured = capfd.readouterr()
    # Should contain the load message and possibly table headers
    assert "No file found or invalid JSON" in captured.out
    # The table might be empty or have headers
    lines = captured.out.strip().split("\n")
    # After the message, there might be table output
    table_lines = [
        line for line in lines if line.strip() and not line.startswith("No file")
    ]
    # Either empty or has headers
    assert len(table_lines) <= 3  # headers or empty


def test_show_transactions_with_data(capfd, sample_transactions):
    # Test showing transactions with data
    service = TransactionService()
    service.transactions = sample_transactions
    service.show_transactions()
    captured = capfd.readouterr()
    output = captured.out
    # Check that output contains expected headers and data
    assert "title" in output
    assert "description" in output
    assert "date" in output
    assert "amount" in output
    assert "type_transaction" in output
    assert "Salary" in output
    assert "Groceries" in output
    assert "5000" in output
    assert "100" in output


def test_show_transactions_by_type_income(capfd, sample_transactions):
    service = TransactionService()
    service.transactions = sample_transactions
    service.show_transactions_by_type("income")
    captured = capfd.readouterr()
    output = captured.out
    assert "Salary" in output
    assert "5000" in output


def test_show_transactions_by_type_expense(capfd, sample_transactions):
    service = TransactionService()
    service.transactions = sample_transactions
    service.show_transactions_by_type("expense")
    captured = capfd.readouterr()
    output = captured.out
    assert "Groceries" in output
    assert "100" in output


def test_show_transactions_by_period_custom(capfd, sample_transactions):
    # Test custom mode with exact date match
    service = TransactionService()
    service.transactions = sample_transactions
    service.show_transactions_by_period("custom", ["2023-10-01"])
    captured = capfd.readouterr()
    output = captured.out
    assert "Salary" in output
    assert "5000" in output
    # Should not include the Groceries transaction
    assert "Groceries" not in output


def test_show_transactions_by_period_custom_range(capfd, sample_transactions):
    # Test custom mode with a start and end date range
    service = TransactionService()
    service.transactions = sample_transactions
    # Provide initial and last dates to capture both transactions in the range
    service.show_transactions_by_period("custom", ["2023-10-01", "2023-10-02"])
    captured = capfd.readouterr()
    output = captured.out
    assert "Salary" in output
    assert "Groceries" in output


def test_show_transactions_by_period_month_year(capfd, sample_transactions):
    # Test month-year mode grouping
    service = TransactionService()
    service.transactions = sample_transactions
    service.show_transactions_by_period("month-year", ["2023-10"])
    captured = capfd.readouterr()
    output = captured.out
    assert "Salary" in output
    assert "Groceries" in output


def test_show_transactions_by_period_year(capfd, sample_transactions):
    # Test year mode grouping
    service = TransactionService()
    service.transactions = sample_transactions
    service.show_transactions_by_period("year", ["2023"])
    captured = capfd.readouterr()
    output = captured.out
    assert "Salary" in output
    assert "Groceries" in output


def test_show_transactions_by_period_none(capfd, sample_transactions):
    # Test no matches return proper message
    service = TransactionService()
    service.transactions = sample_transactions
    service.show_transactions_by_period("custom", ["2022-01-01"])
    captured = capfd.readouterr()
    output = captured.out
    assert "No transactions found for the specified period." in output
