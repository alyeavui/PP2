#1
from functools import reduce

def multiply_list(numbers):
    return reduce(lambda x, y: x * y, numbers)

numbers_input = input()
numbers_str = numbers_input.split()
numbers = [int(num) for num in numbers_str]

result = multiply_list(numbers)
print(result)

#2
def count_upper_lower(text):
    upper_count = sum(1 for char in text if char.isupper())
    lower_count = sum(1 for char in text if char.islower())
    return upper_count, lower_count
text = input()
upper_count, lower_count = count_upper_lower(text)
print("Uppercase letters: ", upper_count)
print("Lowercase letters: ", lower_count)

#3
def is_palindrome(s):
    s = ''.join(e for e in s if e.isalnum()).lower()
    return s == s[::-1]
s = input()
if is_palindrome(s):
    print("Palindrome")
else:
    print("Not a palindrome")

#4
import time
import math
def calculate_square_root(number, milliseconds):
    time.sleep(milliseconds / 1000)
    result = math.sqrt(number)
    return result
number, milliseconds = map(int, input().split())
result = calculate_square_root(number, milliseconds)
print(f"Square root of {number} after {milliseconds} milliseconds is {result}")

#5
def all_true(t):
    return all(t)
t = tuple(bool(int(x)) for x in input().split())
print(all_true(t))