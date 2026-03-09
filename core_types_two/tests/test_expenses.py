# core_types/tests/test_expenses.py

import pytest
from pathlib import Path
from core_types.expenses import load_expenses, save_expenses, add_expense

DATA_FILE = Path("core_types/expenses.json")  # Add this constant for easy reference


@pytest.fixture(autouse=True)
def cleanup():
    # Delete the file before EVERY test
    DATA_FILE.unlink(missing_ok=True)
    yield  # Run the test
    # Optional: delete after too, but not needed since before is enough


def test_add_and_load():
    add_expense(10.0, "Test")
    data = load_expenses()
    assert len(data) == 1
    assert data[0]["amount"] == 10.0
    assert data[0]["category"] == "Test"
