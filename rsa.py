#!/usr/bin/python3

"""
RSA Factoring Challenge

This script reads RSA numbers from a file and attempts to factorize them into their prime factors.
It then prints the factorization results and the time taken.

Usage: rsa.py <file>
where <file> is a file containing RSA numbers to factorize.

Author: Udeme Harrison
"""

import sys
import math
import time

def factorize_rsa_number(number):
    """
    Factorizes a given RSA number into its prime factors.

    Args:
        number (int): The RSA number to be factorized.

    Returns:
        tuple: A tuple containing the two prime factors.
    """
    # Find the smaller prime factor first
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            factor1 = i
            factor2 = number // i
            return factor1, factor2
    return None

def main(filename):
    """
    Main function to read an RSA number from a file and perform factorization.

    Args:
        filename (str): The name of the input file.
    """
    with open(filename, 'r') as file:
        rsa_number = int(file.read())

    start_time = time.time()
    factor1, factor2 = factorize_rsa_number(rsa_number)
    end_time = time.time()

    if factor1 and factor2:
        print(f"{rsa_number}={factor1}*{factor2}")
        print(f"Factorization time: {end_time - start_time:.6f} seconds")
    else:
        print("The given number is not a product of two prime numbers.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: rsa <file>")
        sys.exit(1)

    filename = sys.argv[1]
    main(filename)
