# Module 2 - Chapter 4 Notes: Introducing Python Object Types
Date: [YYYY-MM-DD]
Pages: 75–104

## 1. Why Use Built-in Types? (p76)
- Built-in types are optimized in C → faster and less memory than custom classes.
- They provide "free" operations (indexing, slicing, sorting, etc.).
- Key takeaway: Use built-ins first. Only build your own types when you need something truly custom.

## 2. Python's Core Data Types (p77–78)
Table 4-1 summary:
| Type       | Example literal          | Mutable? | Use case                     |
|------------|--------------------------|----------|------------------------------|
| Numbers    | 123, 3.14, 1+2j          | No       | Math, counters               |
| Strings    | 'spam', "spam", '''...'''| No       | Text, filenames, data        |
| Lists      | [1, 2, 3]                | Yes      | Ordered collections          |
| Dictionaries | {'a':1, 'b':2}         | Yes      | Key-value lookups            |
| Tuples     | (1, 2, 3)                | No       | Fixed records                |
| Files      | open('data.txt')         | —        | Reading/writing data         |

## 3. Numbers (p78)
- Integers have unlimited precision in Python 3.
- Floats are double-precision (watch for 0.1 + 0.2 != 0.3).
- Complex numbers exist but rarely used in beginner code.

## 4. Strings (p80–86)
- Sequence operations: len(), indexing, slicing, concatenation, repetition.
- Immutable → cannot do `s[0] = 'x'`.
- Type-specific methods: `.upper()`, `.split()`, `.strip()`, `.find()`, `.replace()`.
- Getting help: `dir(str)`, `help(str.upper)`.
- Other ways: raw strings `r''`, triple-quoted.
- Pattern matching (regex) — interesting but advanced (p85).

## 5. Lists (p86–90)
- Mutable sequences.
- Operations: append, sort, reverse, pop, index, count.
- Bounds checking (IndexError if out of range).
- Nesting: lists inside lists (matrices).
- List comprehensions ← [expression for value in iterable if condition] 
  Example: `[x**2 for x in range(10) if x % 2 == 0]`

## 6. Dictionaries (p90–96)
- Unordered (until Python 3.7+ insertion order).
- Key must be immutable (string, number, tuple).
- Nesting: dicts inside dicts (very common in real data).
- Sorting keys with `sorted(D.keys())` or `sorted(D)`.
- Missing keys: use `get(key, default)` or `if key in D`.

## 7. Tuples (p96–97)
- Immutable lists → safer for fixed data. (Similar to Lists but ordered and unchangeable)
- Often used for records (e.g., coordinates, RGB colors).
- Utilize with for loops
- Some functions (.count, .index, etc...)

## 8. Files (p97–99)
- `open(filename, 'r')`, `read()`, `readlines()`, `write()`.
- Always close or use `with` statement (we'll improve this later).
- Format (with open(filename) as file) then use various functions listed above.
- Will close file automatically for you.
- Optional use 'try' with 'except' to manage error and keep flow of operation and debug.

## 9. Other Core Types & Flexibility (p99–102)
- Sets, None, Booleans, types themselves.
- "How to break your code's flexibility" → mixing types too wildly or relying on exact object types.

## 10. User-Defined Classes & Everything Else (p101–103)
- Brief preview of OOP (full in Part VI).
- Everything in Python is an object.

## Quiz Answers (p103–104)
1. Name 4 core data types in python: Lists, Dictionaries, Numbers, Booleans
2. Why are they called "core" data types? Because they are commonly used in OOP.
3. What does immutable mean, and which three of the core data types are considered immutable? It means unable to be changed, moved. Manipulated with built-in functions. Tuples, Numbers and Strings are three.
4. What does "sequence" mean, and which three types fall into that category? (Strings, Lists, Dictionaries)
(Write your own answers here — I already did mine in my notebook)
5. What does "mapping" mean and which core tyupe is a mapping? Applies a given function to all items in a collection. Lists
6. What is "polymorphism", and why should you care? Giving many forms to objects either through "inheritance" or "Duck typing".

## Key Takeaways for My Brain
- Prefer built-ins → they are fast, safe, and Pythonic.
- Mutable (lists, dicts) vs Immutable (strings, tuples, numbers).
- Comprehensions = superpower for lists/dicts/sets.
- Nesting = how real data structures are built.

## Project Connection (expenses.py)
- Used list of dicts for expenses.
- Added dict comprehension in `category_summary()`.
- Next: will use tuple for immutable expense records (Ch9).