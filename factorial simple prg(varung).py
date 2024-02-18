# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 20:47:41 2024

@author: varung
"""
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Example usage:
num = int(input("Enter a number to calculate its factorial: "))

if num < 0:
    print("Factorial is not defined for negative numbers.")
elif num == 0:
    print("The factorial of 0 is 1.")
else:
    print(f"The factorial of {num} is {factorial(num)}.")

