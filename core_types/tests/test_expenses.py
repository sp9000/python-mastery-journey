import pytest
from pathlib import Path
from core_types.expenses import (
    load_expenses,
    save_expenses,
    add_expense,
)  # adjust import if needed


@pytest.fixture(autouse=True)
def cleanup():
    yield
    Path("core_types/expenses.json").unlink(missing_ok=True)


def test_add_and_load():
    add_expense(10.0, "Test")
    data = load_expenses()
    assert len(data) == 1
    assert data[0]["amount"] == 10.0
    assert data[0]["category"] == "Test"
