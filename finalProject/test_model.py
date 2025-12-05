import pytest
from pydantic import ValidationError
from model import Transaction
from datetime import datetime


def test_valid_transaction():
    # Test creating a valid transaction
    transaction = Transaction(
        title="Salary",
        description="Monthly salary",
        date=datetime(2023, 10, 1),
        tags=["work", "income"],
        amount=5000.0,
        type_transaction="income",
    )
    assert transaction.title == "Salary"
    assert transaction.description == "Monthly salary"
    assert transaction.amount == 5000.0
    assert transaction.type_transaction == "income"
    assert transaction.tags == ["work", "income"]


def test_valid_expense_transaction():
    # Test creating a valid expense transaction
    transaction = Transaction(
        title="Groceries",
        description="Weekly groceries",
        date=datetime(2023, 10, 2),
        tags=None,
        amount=100.0,
        type_transaction="expense",
    )
    assert transaction.title == "Groceries"
    assert transaction.description == "Weekly groceries"
    assert transaction.amount == 100.0
    assert transaction.type_transaction == "expense"
    assert transaction.tags is None


def test_invalid_amount_zero():
    # Test that amount cannot be zero
    with pytest.raises(ValidationError):
        Transaction(
            title="Test",
            description="Test",
            date=datetime(2023, 10, 1),
            amount=0,
            type_transaction="income",
        )  # type: ignore


def test_invalid_amount_negative():
    # Test that amount cannot be negative
    with pytest.raises(ValidationError):
        Transaction(
            title="Test",
            description="Test",
            date=datetime(2023, 10, 1),
            amount=-100.0,
            type_transaction="income",
        )  # type: ignore


def test_invalid_type_transaction():
    # Test that type_transaction must be "income" or "expense"
    with pytest.raises(ValidationError):
        Transaction(
            title="Test",
            description="Test",
            date=datetime(2023, 10, 1),
            amount=100.0,
            type_transaction="transfer",
        )  # type: ignore


def test_title_too_long():
    # Test that title cannot exceed 70 characters
    long_title = "a" * 71
    with pytest.raises(ValidationError):
        Transaction(
            title=long_title,
            description="Test",
            date=datetime(2023, 10, 1),
            amount=100.0,
            tags=["test"],
            type_transaction="income",
        )


def test_description_too_long():
    # Test that description cannot exceed 255 characters
    long_description = "a" * 256
    with pytest.raises(ValidationError):
        Transaction(
            title="Test",
            description=long_description,
            date=datetime(2023, 10, 1),
            amount=100.0,
            tags=["test"],
            type_transaction="income",
        )


def test_title_max_length():
    # Test that title can be exactly 70 characters
    max_title = "a" * 70
    transaction = Transaction(
        title=max_title,
        description="Test",
        date=datetime(2023, 10, 1),
        tags=None,
        amount=100.0,
        type_transaction="income",
    )
    assert transaction.title == max_title


def test_description_max_length():
    # Test that description can be exactly 255 characters
    max_description = "a" * 255
    transaction = Transaction(
        title="Test",
        description=max_description,
        date=datetime(2023, 10, 1),
        tags=None,
        amount=100.0,
        type_transaction="income",
    )
    assert transaction.description == max_description


def test_invalid_date():
    # Test that date must be a valid datetime
    with pytest.raises(ValidationError):
        Transaction(
            title="Test",
            description="Test",
            date="invalid date",  # type: ignore
            tags=None,
            amount=100.0,
            type_transaction="income",
        )
