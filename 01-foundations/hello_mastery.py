#!/usr/bin/env python3
"""
My first Python Mastery script
Learning Python 4th Edition - Module 1
"""

print("🚀 Python Mastery Journey Started!")
print("Book: Learning Python, 4th Edition by Mark Lutz")
print("Current goal: Go from Beginner → Production AI Agent Engineer")

# Make input optional for CI
import sys

if sys.stdin.isatty():
    name = input("What is your name? ")
else:
    name = "CI Runner"  # default when running in GitHub Actions

print(f"Welcome, {name}! You are now on Module 1.")

# Quick demo of Python running
import sys

print(f"Python version: {sys.version}")
print("✅ Script ran successfully in CI!")
