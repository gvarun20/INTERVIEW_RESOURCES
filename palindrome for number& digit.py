# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 20:59:13 2024

@author: varung
"""
def is_palindrome(input_str):
    clean_str = ''.join(char.lower() for char in str(input_str) if char.isalnum())
    return clean_str == clean_str[::-1]

# Example usage:
user_input = input("Enter a string or number to check if it's a palindrome: ")
if is_palindrome(user_input):
    print(f"{user_input} is a palindrome.")
else:
    print(f"{user_input} is not a palindrome.")

