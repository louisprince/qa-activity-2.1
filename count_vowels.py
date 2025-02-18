#!/bin/python3

VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')
vowels_in_word = 0

chosen_word = input("Please input a word: ")
for letter in chosen_word:
    if letter in VOWELS:
        letter = "!"
        vowels_in_word += 1

print(f"The total number of vowels in the word \"{chosen_word}\" is {vowels_in_word}")
