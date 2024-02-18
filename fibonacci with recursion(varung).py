# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 20:25:33 2024

@author: varun g

"""
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Example usage:
terms = int(input("Enter the number of terms in the Fibonacci series: "))

if terms <= 0:
    print("Please enter a positive integer.")
else:
    print("Fibonacci series:")
    for i in range(terms):
        print(fibonacci(i), end=" ")

