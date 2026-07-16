# Module 2 - Chapter 5 Notes: Numeric Types
Date: 3-11-26
Pages: 105–142

## 1. Numeric Type Basics (p105–106)
- Integers (int): unlimited size in Python 3.
- Floats (float): double precision.
- Complex (complex): real + imaginary (e.g., 1+2j).

## 2. Integers (p106–108)
- Literals: 123, 0b101 (binary), 0o77 (octal), 0xAF (hex).
- Operations: + - * / // % **.

## 3. Floating-Point Numbers (p108–110)
- Literals: 3.14, 1e-3.
- Precision issues: 0.1 + 0.2 != 0.3 (use decimal for money).

## 4. Complex Numbers (p110–111)
- Literals: 1+2j.
- Methods: .real, .imag, .conjugate().

## 5. Numeric Operators and Functions (p111–113)
- Basic: arithmetic, comparison.
- Functions: abs(), divmod(), pow(), round().

## 6. Numeric Display Formats (p113–115)
- str(), repr(), format().

## 7. Comparisons: Normal and Chained (p115–116)
- 1 < 2 < 3 (chained).

## 8. Integer Precision (p116–117)
- No overflow — bigints automatic.

## 9. Division: Classic, Floor, True (p117–121)
- / true division (float), // floor (int).

## 10. Hexadecimal, Octal, Binary Notation (p122–123)
- bin(), hex(), oct().

## 11. Bitwise Operations (p123–125)
- & | ^ ~ << >> (binary ops).

## 12. Other Built-in Numeric Tools (p125–127)
- math module, random.

## 13. Fraction Type (p127–129)
- from fractions import Fraction.

## 14. Sets (p129–133)
- {1,2,3}, operations: union, intersection.

## 15. Booleans (p133–139)
- True/False = 1/0.

## 16. Numeric Extensions (p139–140)
- Third-party libs (NumPy, etc.).

## Quiz Answers (p141–142)
1. ...
(Your answers here)

## Key Takeaways
- Handle floats carefully for money (use Decimal).
- Bitwise for low-level stuff.
- Sets for unique items.

## Project Connection (expenses.py)
- Updated amounts to use Decimal for precision.
- Added total calculation with rounding.