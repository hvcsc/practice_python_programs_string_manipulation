"""Prog06: Create a program that ask the user to input their fullname in
incorrect casing. Print each character of the input in reverse casing.
Example:
Input: jUAn DEla CrUZ
Output: JuaN deLA cRuz"""

#ask name then reverse
fullname = input("Enter your full name in incorrect casing: ").swapcase()

#print the reverse casing
print(fullname)