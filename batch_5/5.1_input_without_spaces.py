"""Prog01: Create a program that ask the user to input their fullname with several space
characters at the beginning. Print the input without the spaces in the beginning.
Example:
Input:         Juan Dela Cruz
Output: Juan Dela Cruz"""

#ask users input
user = input("Enter your full name: ")

#remove spaces
no_space = user.lstrip()

#print input without the spaces at the beginning