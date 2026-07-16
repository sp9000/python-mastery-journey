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


def main() -> None:
    """Main entry point for the CLI application."""
    parser = argparse.ArgumentParser(
        description="Personal Finance Tracker - Practice Core Data Types",
        epilog="Use 'add', 'list', 'total', or 'summary' commands"
    )

    # Create subparsers for different commands (like git add, git commit)
    subparsers = parser.add_subparsers(
        dest="command",           # This will store which command was used
        required=True,            # Force user to pick a command
        help="Available commands"
    )

    # === ADD COMMAND ===
    add_parser = subparsers.add_parser("add", help="Add a new expense")
    add_parser.add_argument("amount", type=float, help="Expense amount (e.g. 12.50)")
    add_parser.add_argument("category", type=str, help="Expense category (e.g. Coffee)")
    add_parser.add_argument("--date", type=str, help="Date in YYYY-MM-DD format (optional)")

    # === LIST COMMAND ===
    subparsers.add_parser("list", help="List all expenses")

    # === TOTAL COMMAND ===
    total_parser = subparsers.add_parser("total", help="Show total expenses")
    total_parser.add_argument("--category", type=str, help="Filter by category")

    # === SUMMARY COMMAND ===
    subparsers.add_parser("summary", help="Show spending by category")

    # Parse the arguments
    args = parser.parse_args()

    # Route to the right function based on command
    if args.command == "add":
        print(f"Would add expense: ${args.amount} in category '{args.category}'")
    elif args.command == "list":
        print("Would list all expenses")
    elif args.command == "total":
        print(f"Would show total (category filter: {args.category})")
    elif args.command == "summary":
        print("Would show category summary")


if __name__ == "__main__":
    main()