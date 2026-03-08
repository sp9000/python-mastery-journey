#!/usr/bin/env python3
"""
Personal Finance Tracker
Module 2 - Core Data Types (Learning Python 4th Ed.)
"""

import argparse
import json
from pathlib import Path
from datetime import date
from typing import List, Dict, Any

DATA_FILE = Path("02-core-types/expenses.json")


def load_expenses() -> List[Dict[str, Any]]:
    if DATA_FILE.exists():
        return json.loads(DATA_FILE.read_text(encoding="utf-8"))
    return []


def save_expenses(expenses: List[Dict[str, Any]]) -> None:
    DATA_FILE.parent.mkdir(exist_ok=True)
    DATA_FILE.write_text(json.dumps(expenses, indent=2), encoding="utf-8")


def add_expense(amount: float, category: str, date_str: str = None) -> None:
    expenses = load_expenses()
    entry = {
        "amount": round(float(amount), 2),
        "category": category.strip(),
        "date": date_str or str(date.today()),
    }
    expenses.append(entry)
    save_expenses(expenses)
    print(f"✅ Added ${entry['amount']:.2f} to '{entry['category']}'")


def list_expenses() -> None:
    expenses = load_expenses()
    if not expenses:
        print("No expenses yet.")
        return
    for i, e in enumerate(expenses, 1):
        print(f"{i:2d}. ${e['amount']:>7.2f}  {e['date']:10}  {e['category']}")


def total_expenses(category: str = None) -> None:
    expenses = load_expenses()
    if category:
        total = sum(
            e["amount"] for e in expenses if e["category"].lower() == category.lower()
        )
        print(f"Total for '{category}': ${total:.2f}")
    else:
        total = sum(e["amount"] for e in expenses)
        print(f"Grand total: ${total:.2f}")


def category_summary() -> None:
    """Show dictionary of {category: total} using dict comprehension"""
    expenses = load_expenses()
    summary = {
        cat: sum(e["amount"] for e in expenses if e["category"] == cat)
        for cat in {e["category"] for e in expenses}
    }
    if not summary:
        print("No expenses yet.")
        return
    print("📊 Category Summary:")
    for cat, total in sorted(summary.items()):
        print(f"  {cat:12} : ${total:.2f}")


def main():
    parser = argparse.ArgumentParser(description="Personal Finance Tracker - Module 2")
    sub = parser.add_subparsers(
        dest="command", required=True, help="Available commands"
    )

    # Add
    add_p = sub.add_parser("add", help="Add a new expense")
    add_p.add_argument("amount", type=float)
    add_p.add_argument("category", type=str)
    add_p.add_argument("--date", type=str, help="YYYY-MM-DD")

    # List
    sub.add_parser("list", help="List all expenses")

    # Total
    total_p = sub.add_parser("total", help="Show grand total")
    total_p.add_argument("--category", type=str, help="Filter by category")

    # Summary (NEW!)
    sub.add_parser(
        "summary", help="Show spending by category (dict comprehension demo)"
    )

    args = parser.parse_args()

    if args.command == "add":
        add_expense(args.amount, args.category, getattr(args, "date", None))
    elif args.command == "list":
        list_expenses()
    elif args.command == "total":
        total_expenses(getattr(args, "category", None))
    elif args.command == "summary":
        category_summary()


if __name__ == "__main__":
    main()
