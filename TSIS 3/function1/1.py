#task 1
def grams_to_ounces(grams):
    ounces = 28.3495231 * grams
    return ounces

grams_needed = int(input())
ounces_needed = grams_to_ounces(grams_needed)
print(ounces_needed)

#task 2
def fahrenheit_to_celsius(fahrenheit):
    celsius = (5 / 9) * (fahrenheit - 32)
    return celsius
fahrenheit_temp = float(input())
celsius_temp = fahrenheit_to_celsius(fahrenheit_temp)
print(celsius_temp)

#task 3
def solve(numheads, numlegs):
    for num_chickens in range(numheads + 1):
        num_rabbits = numheads - num_chickens
        if (2 * num_chickens + 4 * num_rabbits) == numlegs:
            return num_chickens, num_rabbits
numheads = int(input())
numlegs = int(input())
chickens, rabbits = solve(numheads, numlegs)
print("Number of chickens:", chickens)
print("Number of rabbits:", rabbits)

#task 4
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]

input_numbers = input()
numbers_list = list(map(int, input_numbers.split()))
prime_numbers = filter_prime(numbers_list)
print(prime_numbers)

#task 5
from itertools import permutations
def print_permutations(string):
    perms = permutations(string)
    for perm in perms:
        print(''.join(perm))
user_input = input()
print_permutations(user_input)

#task 6
def reverse_sentence(sentence):
    words = sentence.split()
    reversed_words = reversed(words)
    reversed_sentence = ' '.join(reversed_words)
    return reversed_sentence
s = input()
reversed_sentence = reverse_sentence(s)
print(reversed_sentence)

#task 7
def has_adjacent_3(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False
numbers = input()
numbers_list = list(map(int, numbers.split()))
print(has_adjacent_3(numbers_list)) 

#task 8
def spy_game(nums):
    position = 0
    for num in nums:
        if num == 0:
            position += 1
        elif num == 7:
            if position == 2:
                return True
    return False
numbers = input()
numbers_list = list(map(int, numbers.split()))
print(spy_game(numbers_list))

#task 9
import math
def sphere_volume(radius):
    volume = (4/3) * math.pi * (radius ** 3)
    return volume
radius = int(input())
volume = sphere_volume(radius)
print(volume)

#task 10
def unique_elements(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

numbers = input()
numbers_list = list(map(int, numbers.split()))
unique_list = unique_elements(numbers_list)
print(unique_list)

#task 11
def is_palindrome(word):
    word = word.lower().replace(" ", "")
    return word == word[::-1]

word = input()
print(is_palindrome(word))

#task 12
def histogram():
    numbers_str = input()
    numbers = [int(num) for num in numbers_str.split()]

    for num in numbers:
        print('*' * num)

histogram()

#task 13
import random

def guess_the_number():
    print("Hello! What is your name?")
    name = input().strip()
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")

    secret_number = random.randint(1, 20)
    num_guesses = 0

    while True:
        print("Take a guess.")
        guess = int(input())

        num_guesses += 1

        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            break

    print(f"Good job, {name}! You guessed my number in {num_guesses} guesses!")

guess_the_number()

