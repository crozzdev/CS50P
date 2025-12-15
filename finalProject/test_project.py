from datetime import datetime
from project import (
    get_title,
    get_description,
    get_date_from_user,
    get_tags,
    get_amount,
    get_type_transaction,
    get_mode_period,
    get_key_dates,
    get_user_transaction_id,
    confirm_transaction_deletion,
    confirm_data_deletion,
)


class TestGetTitle:
    def test_valid_title(self, monkeypatch):
        monkeypatch.setattr("builtins.input", lambda _: "Valid Title")
        assert get_title() == "Valid Title"

    def test_title_too_short_then_valid(self, monkeypatch):
        inputs = iter(["abc", "Valid Title"])
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))
        assert get_title() == "Valid Title"


class TestGetDescription:
    def test_valid_description(self, monkeypatch):
        monkeypatch.setattr("builtins.input", lambda _: "This is a valid description")
        assert get_description() == "This is a valid description"

    def test_description_too_long_then_valid(self, monkeypatch):
        long_desc = "a" * 256
        inputs = iter([long_desc, "Valid description"])
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))
        assert get_description() == "Valid description"


class TestGetDateFromUser:
    def test_valid_date_yyyy_mm_dd(self, monkeypatch):
        monkeypatch.setattr("builtins.input", lambda _: "2023-10-01")
        result = get_date_from_user()
        assert result == datetime(2023, 10, 1)

    def test_valid_date_mm_dd_yyyy(self, monkeypatch):
        monkeypatch.setattr("builtins.input", lambda _: "10/01/2023")
        result = get_date_from_user()
        assert result == datetime(2023, 10, 1)

    def test_valid_date_dd_mm_yyyy(self, monkeypatch):
        monkeypatch.setattr("builtins.input", lambda _: "10/01/2023")
        result = get_date_from_user()
        assert result == datetime(2023, 10, 1)

    def test_valid_date_yyyy_slash_mm_slash_dd(self, monkeypatch):
        monkeypatch.setattr("builtins.input", lambda _: "2023/10/01")
        result = get_date_from_user()
        assert result == datetime(2023, 10, 1)

    def test_invalid_date_then_valid(self, monkeypatch):
        inputs = iter(["invalid", "2023-10-01"])
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))
        result = get_date_from_user()
        assert result == datetime(2023, 10, 1)


class TestGetTags:
    def test_valid_tags(self, monkeypatch):
        monkeypatch.setattr("builtins.input", lambda _: "tag1,tag2,tag3")
        assert get_tags() == ["tag1", "tag2", "tag3"]

    def test_empty_tags(self, monkeypatch):
        monkeypatch.setattr("builtins.input", lambda _: "")
        assert get_tags() == [""]

    def test_tags_with_spaces(self, monkeypatch):
        monkeypatch.setattr("builtins.input", lambda _: "tag1, tag2 , tag3")
        assert get_tags() == ["tag1", "tag2", "tag3"]

    def test_tags_with_multiple_spaces(self, monkeypatch):
        monkeypatch.setattr("builtins.input", lambda _: "tag1,  tag2,   tag3")
        assert get_tags() == ["tag1", "tag2", "tag3"]


class TestGetAmount:
    def test_valid_amount(self, monkeypatch):
        monkeypatch.setattr("builtins.input", lambda _: "100.50")
        assert get_amount() == 100.50

    def test_zero_amount_then_valid(self, monkeypatch):
        inputs = iter(["0", "100.50"])
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))
        assert get_amount() == 100.50

    def test_negative_amount_then_valid(self, monkeypatch):
        inputs = iter(["-10", "100.50"])
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))
        assert get_amount() == 100.50

    def test_invalid_input_then_valid(self, monkeypatch):
        inputs = iter(["abc", "100.50"])
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))
        assert get_amount() == 100.50


class TestGetTypeTransaction:
    def test_valid_income(self, monkeypatch):
        monkeypatch.setattr("builtins.input", lambda _: "Income")
        assert get_type_transaction() == "income"

    def test_valid_expense(self, monkeypatch):
        monkeypatch.setattr("builtins.input", lambda _: "Expense")
        assert get_type_transaction() == "expense"

    def test_valid_income_lowercase(self, monkeypatch):
        monkeypatch.setattr("builtins.input", lambda _: "income")
        assert get_type_transaction() == "income"


class TestGetModePeriodAndKeyDates:
    def test_get_mode_period_valid(self, monkeypatch):
        monkeypatch.setattr("builtins.input", lambda _: "custom")
        assert get_mode_period() == "custom"

    def test_get_mode_period_invalid_then_valid(self, monkeypatch):
        inputs = iter(["invalid", "month-year"])
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))
        assert get_mode_period() == "month-year"

    def test_get_key_dates_custom_single(self, monkeypatch):
        monkeypatch.setattr("builtins.input", lambda _: "2023-10-01")
        assert get_key_dates("custom") == ["2023-10-01"]

    def test_get_key_dates_custom_range(self, monkeypatch):
        # Input two dates separated by a comma for a range
        monkeypatch.setattr("builtins.input", lambda _: "2023-10-01, 2023-10-02")
        assert get_key_dates("custom") == ["2023-10-01", "2023-10-02"]

    def test_get_key_dates_month_year(self, monkeypatch):
        monkeypatch.setattr("builtins.input", lambda _: "2023-10")
        assert get_key_dates("month-year") == ["2023-10"]

    def test_get_key_dates_year(self, monkeypatch):
        monkeypatch.setattr("builtins.input", lambda _: "2023")
        assert get_key_dates("year") == ["2023"]

    def test_get_key_dates_invalid_then_valid(self, monkeypatch):
        inputs = iter(["invalid-date", "2023-10-01"])
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))
        assert get_key_dates("custom") == ["2023-10-01"]

    def test_invalid_type_then_valid(self, monkeypatch):
        inputs = iter(["invalid", "Income"])
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))
        assert get_type_transaction() == "income"


class TestGetUserTransactionId:
    def test_valid_index(self, monkeypatch):
        monkeypatch.setattr("builtins.input", lambda _: "1")
        transactions = [None, None, None]
        assert get_user_transaction_id(transactions) == 1  # type: ignore

    def test_invalid_input_then_valid(self, monkeypatch):
        inputs = iter(["abc", "2"])
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))
        transactions = [None, None, None]
        assert get_user_transaction_id(transactions) == 2  # type: ignore

    def test_out_of_range_then_valid(self, monkeypatch):
        inputs = iter(["10", "0"])
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))
        transactions = [None]
        assert get_user_transaction_id(transactions) == 0  # type: ignore


class TestConfirmTransactionDeletion:
    def test_confirm_yes(self, monkeypatch):
        monkeypatch.setattr("builtins.input", lambda _: "Y")
        transactions = ["t0", "t1"]
        assert confirm_transaction_deletion(1, transactions) is True  # type: ignore

    def test_confirm_no_prints_and_returns_false(self, monkeypatch, capsys):
        monkeypatch.setattr("builtins.input", lambda _: "no")
        transactions = ["t0"]
        result = confirm_transaction_deletion(0, transactions)  # type: ignore
        assert result is False
        captured = capsys.readouterr()
        assert "As you didn't confirm, the operation was cancelled" in captured.out


class TestConfirmDataDeletion:
    def test_confirm_yes(self, monkeypatch):
        monkeypatch.setattr("builtins.input", lambda _: "delete")
        assert confirm_data_deletion() is True

    def test_confirm_no_prints_and_returns_false(self, monkeypatch, capsys):
        monkeypatch.setattr("builtins.input", lambda _: "n")
        result = confirm_data_deletion()
        assert result is False
        captured = capsys.readouterr()
        assert (
            "As you didn't confirm, the operation was cancelled and no data was deleted"
            in captured.out
        )
