# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 20:50:37 2024

@author: varung 


"""
def print_pattern(rows):
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

# Example usage:
num_rows = int(input("Enter the number of rows for the pattern: "))
print_pattern(num_rows)

