#!/bin/python3

# Task: List Comprehension Practice
# You are given a list of numbers. Your goal is to complete the following tasks using list comprehensions:

example_list = [32, 54, 75, 43, 2, 5, 87, 9, 2, 12, 13, 15, 645, 85, 3745, 34, 90, 87, 91, 93, 54, 53, 754, 324, 432, 765, 765, 345]
print(f"Example list: {example_list}")

# Create a new list containing only the even numbers from the original list.
even_numbers = [x for x in example_list if x % 2 == 0]
print(f"Even numbers: {even_numbers}")

# Create a new list containing the squares of the even numbers from the original list.
squared_evens = [x**2 for x in example_list if x % 2 == 0]
print(f"Squared even numbers: {squared_evens}")

# Create a new list containing only the numbers that are divisible by 3 but not by 5 from the original list.
factor_3_not_5 = [x for x in example_list if x % 3 == 0 and x % 5 != 0]
print(f"The nubers which are divisible by 3 but not divisible by 5: {factor_3_not_5}")

# Create a new list containing the words in a sentence that are longer than 4 characters (ignoring case).
example_sentence = "The Quick Brown Fox Jumps Over The Lazy Dog"
longer_than_4_characters = [word.lower() for word in example_sentence.split(' ') if len(word) > 4]
print(f"Words with more than 4 characters: {longer_than_4_characters}")

# Create a new list containing the first letter of each word in a sentence (ignore punctuation).
first_letters = [letter[0:1] for letter in example_sentence.split(' ')]
print(f"The first letter of each word: {first_letters}")

# Create a dictionary where each country is a key and its capital city is the value.
countries_and_cities = [
    ("USA", "Washington, D.C."),
    ("Canada", "Ottawa"),
    ("Japan", "Tokyo"),
    ("Germany", "Berlin"),
    ("France", "Paris"),
    ("Italy", "Rome"),
    ("Australia", "Canberra"),
    ("India", "New Delhi"),
    ("Brazil", "Brasília"),
    ("Russia", "Moscow")
]

capital_cities = {country: city for country, city in countries_and_cities}
for country in capital_cities:
    print(f"The capital city of {country} is {capital_cities[country]}")
