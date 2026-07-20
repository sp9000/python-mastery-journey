#!/usr/bin/env python3
"""
Personal Finance Tracker
Module 2 - Core Data Types (Learning Python 4th Edition)
"""

import argparse
import json
from pathlib import Path
from datetime import date
from typing import List, Dict, Any

# Global data file path
DATA_FILE = Path("core_types_two/expenses.json")


def load_expenses() -> List[Dict[str, Any]]:
    """Load expenses from JSON file. Return empty list if file doesn't exist."""
    if DATA_FILE.exists():
        try:
            return json.loads(DATA_FILE.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, IOError):
            print("Warning: Could not read expenses file. Starting fresh.")
            return []
    return []


def save_expenses(expenses: List[Dict[str, Any]]) -> None:
    """Save expenses list to JSON file."""
    DATA_FILE.parent.mkdir(exist_ok=True)  # Ensure directory exists
    DATA_FILE.write_text(
        json.dumps(expenses, indent=2, ensure_ascii=False),
        encoding="utf-8"
    )

# ==================== COMMAND FUNCTIONS ====================

def add_expense(amount: float, category: str, date_str: str = None) -> None:
    """Add a new expense and save it."""
    try:
        # Validate amount (Chapter 5 numeric concepts)
        amount = float(amount)
        if amount <= 0:
            print("❌ Error: Amount must be greater than zero.")
            return
        
        # Validate category
        category = category.strip()
        if not category:
            print("❌ Error: Category cannot be empty.")
            return
    
        expenses = load_expenses()
    
        entry = {
         "amount": round(float(amount), 2),
           "category": category.strip(),
           "date": date_str or str(date.today())
      }
    
        expenses.append(entry)
        save_expenses(expenses)
    
        print(f"✅ Added ${entry['amount']:.2f} to '{entry['category']}' on {entry['date']}")

    except (ValueError, TypeError):
        print("❌ Error: Amount must be a valid number.")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

def list_expenses() -> None:
    """List all expenses."""
    expenses = load_expenses()
    if not expenses:
        print("No expenses yet.")
        return
    for i, e in enumerate(expenses, 1):
        print(f"{i:2d}. ${e['amount']:>7.2f}  {e['date']:10}  {e['category']}")


def total_expenses(category: str = None) -> None:
    """Show total expenses, optionally filtered by category."""
    expenses = load_expenses()
    if category:
        total = sum(e["amount"] for e in expenses if e["category"].lower() == category.lower())
        print(f"Total for '{category}': ${total:.2f}")
    else:
        total = sum(e["amount"] for e in expenses)
        print(f"Grand total: ${total:.2f}")


def summary_expenses() -> None:
    """Show summary by category using dict comprehension."""
    expenses = load_expenses()
    if not expenses:
        print("No expenses yet.")
        return
    
    summary = {
        cat: sum(e["amount"] for e in expenses if e["category"] == cat)
        for cat in {e["category"] for e in expenses}
    }
    
    print("📊 Category Summary:")
    for cat, total in sorted(summary.items()):
        print(f"  {cat:12} : ${total:.2f}")


def main() -> None:
    """Main entry point for the CLI application."""
    parser = argparse.ArgumentParser(
        description="Personal Finance Tracker - Practice Core Data Types",
        epilog="Use 'add', 'list', 'total', or 'summary' commands"
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True,
        help="Available commands"
    )

    # === ADD COMMAND ===
    add_parser = subparsers.add_parser("add", help="Add a new expense")
    add_parser.add_argument("amount", type=str, help="Expense amount (e.g. 12.50)")
    add_parser.add_argument("category", type=str, help="Expense category (e.g. Coffee)")
    add_parser.add_argument("--date", type=str, help="Date in YYYY-MM-DD format (optional)")

    # === LIST COMMAND ===
    subparsers.add_parser("list", help="List all expenses")

    # === TOTAL COMMAND ===
    total_parser = subparsers.add_parser("total", help="Show total expenses")
    total_parser.add_argument("--category", type=str, help="Filter by category")

    # === SUMMARY COMMAND ===
    subparsers.add_parser("summary", help="Show spending by category")

    args = parser.parse_args()

    # === COMMAND ROUTING ===
    if args.command == "add":
        add_expense(args.amount, args.category, args.date)
    elif args.command == "list":
        list_expenses()
    elif args.command == "total":
        total_expenses(args.category)
    elif args.command == "summary":
        summary_expenses()


if __name__ == "__main__":
    main()