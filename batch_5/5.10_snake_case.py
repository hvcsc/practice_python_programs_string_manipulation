"""Prog10: Create a program that ask the user to input their fullname in
incorrect casing. Print the input in snake case.
Example:
Input: jUAn DEla CrUZ
Output: juan_dela_cruz"""

#ask name
fullname = input("Enter your name in incorrect casing: ").lower()

#change space to underscore
snake = fullname.replace(" ", "_")

#print snake case
print(snake)