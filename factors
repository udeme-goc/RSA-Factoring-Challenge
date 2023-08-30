#!/usr/bin/python3

"""
Factors Challenge

This script reads natural numbers from a file and attempts
to factorize them into products of smaller numbers.
It then prints the factorization results.

Usage: factors.py <file>
where <file> is a file containing natural numbers to factorize.

Author: Udeme Harrison
"""

import sys
import math

def factorize(number):
    """
    Factorizes a number into its prime factors.

    Args:
        number (int): The number to be factorized.
    """
    for i in range(2, int(math.sqrt(number)) + 1):
        while number % i == 0:
            print(f"{number}={i}*{number // i}")
            number //= i
    if number > 1:
        print(f"{number}={number}*1")

def main(input_filename):
    """
    Main function to read natural numbers from a file and perform factorization.

    Args:
        input_filename (str): The name of the input file.
    """
    with open(input_filename, 'r') as file:
        for line in file:
            number = int(line.strip())
            factorize(number)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: factors.py <file>")
        sys.exit(1)

    input_filename = sys.argv[1]
    main(input_filename)
