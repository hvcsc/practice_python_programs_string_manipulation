"""Prog02: Create a program that ask the user to input a number (0-1000).
Print the number in 6 digit format. Add zeros at the beginning to complete the 6 digit.
Example:
Input: 143
Output: 000143"""

#ask input
num = int(input("Enter a number (0-1000): "))

#change format
num = f"{num:06}"

#print 6 format digit
