# ==================== Chapter 4: Intro to Python Object Types  ====================

# List Comprehension Expression
# ===============================

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Old-school way (what you'd do in other languages)
squares = []
for n in numbers:
    squares.append(n**2)

# Pythonic way — one clean line!
squares_comp = [n**2 for n in numbers]

# With filtering (only even numbers)
evens_squared = [n**2 for n in numbers if n % 2 == 0]

print("All squares:", squares_comp)
print("Even squares:", evens_squared)


# ==================== Chapter 5: Numeric Types ====================

# ==================== Chapter 7: Strings ====================
