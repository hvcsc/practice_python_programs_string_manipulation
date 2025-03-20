"""Prog09: Create a program that ask the user to input their fullname in
incorrect casing. Print the input in pascal case.
Example:
Input: jUAn DEla CrUZ
Output: JuanDelaCruz"""

#ask name
fullname = input("Enter your fullname in incorrect casing: ")

#change to pascal casing
pascal = fullname.title().replace(" ", "")

#print name
print(pascal)