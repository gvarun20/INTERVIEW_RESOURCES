# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 21:01:36 2024

@author: varung
"""
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Example usage:
user_year = int(input("Enter a year to check if it's a leap year: "))
print(f"{user_year} is {'a leap year' if is_leap_year(user_year) else 'not a leap year'}.")

