# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 20:53:32 2024

@author: varung
"""
def sum_of_digits(number):
    num_str = str(number)
    digit_sum = 0
    for digit in num_str:
        digit_sum += int(digit)
    return digit_sum

num = int(input("Enter a number to calculate the sum of its digits: "))
result = sum_of_digits(num)
print(f"The sum of digits in {num} is {result}.")

