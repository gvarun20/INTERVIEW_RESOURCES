# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 20:28:27 2024

@author: varung
"""
def fibonacci(n):
    fib_series = [0, 1]
    
    for i in range(2, n):
        fib_series.append(fib_series[i-1] + fib_series[i-2])
    
    return fib_series

# Example usage:
terms = int(input("Enter the number of terms in the Fibonacci series: "))

if terms <= 0:
    print("Please enter a positive integer.")
else:
    result = fibonacci(terms)
    print("Fibonacci series:", result)

