"""Prog05: Create a program that ask the user to input their fullname in
incorrect casing. Print the input in proper casing.
Example:
Input: jUAn DEla CrUZ
Output: Juan Dela Cruz"""

#ask name then correct the casing
fullname = input("Enter your full name in incorrect casing: ").title()

#print the proper casing
print(fullname)