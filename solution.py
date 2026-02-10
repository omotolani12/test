# ---------------------------------------------------------------------
# Problem 01: Return even numbers
# ---------------------------------------------------------------------
"""
Problem 01:
Write a function that returns all even numbers from a list.

Example:
find_even_numbers([1, 2, 3, 4, 5, 6]) -> [2, 4, 6]
"""

def find_even_numbers(nums):
    evens = []
    for n in nums:
        if n % 2 == 0:
            evens.append(n)
    return evens


# ---------------------------------------------------------------------
# Problem 02: Generate Fibonacci series
# ---------------------------------------------------------------------
"""
Problem 02:
Write a function that returns the first n numbers in the Fibonacci sequence.

Example:
fibonacci(5) -> [0, 1, 1, 2, 3]
"""

def fibonacci(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]
    seq = [0, 1]
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    return seq


# ---------------------------------------------------------------------
# Problem 03: Count word frequency
# ---------------------------------------------------------------------
"""
Problem 03:
Write a function that counts how many times each word appears in a list.

Example:
count_words(["a", "b", "a"]) -> {"a": 2, "b": 1}
"""

def count_words(words):
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts


# ---------------------------------------------------------------------
# Problem 04: Remove duplicates while preserving order
# ---------------------------------------------------------------------
"""
Problem 04:
Write a function that removes duplicates from a list while preserving order.

Example:
remove_duplicates([1, 2, 1, 3]) -> [1, 2, 3]
"""

def remove_duplicates(items):
    seen = set()
    unique = []
    for item in items:
        if item not in seen:
            unique.append(item)
            seen.add(item)
    return unique


# ---------------------------------------------------------------------
# Problem 05: Palindrome check
# ---------------------------------------------------------------------
"""
Problem 05:
Write a function that returns True if a string is a palindrome.
Input is string of characters.

Example:
is_palindrome("level") -> True
is_palindrome("hello") -> False
"""

def is_palindrome(text):
    return text == text[::-1]


# ---------------------------------------------------------------------
# Problem 06: Safe division
# ---------------------------------------------------------------------
"""
Problem 06:
Write a function that divides a by b and returns None if division is not possible.

Example:
safe_divide(10, 2) -> 5.0
safe_divide(10, 0) -> None
"""

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None


if __name__ == "__main__":
    # print(find_even_numbers([1, 2, 3, 4, 5, 6, 7]))
    # print(fibonacci(5))
    # print(count_words(["a", "b", "a"]))
    # print(remove_duplicates([1, 2, 1, 3]))
    # print(is_palindrome("level"))
    # print(safe_divide(10, 0))
    # print(safe_divide(10, "a"))
    pass
