"""This program will output all numbers in a given range (default is 1 to 100) and tell us if the number is prime or not.

Programmer: David Weinstein
Date: 10/30/2019
File name: prime_numbers_weinstein.py

Pseudocode:
1.
"""

def is_prime(num):
    if num < 0:
        return False
    else:
        for x in range(2, num):
            if num % x == 0:
                return "Not Prime"
    return "Prime"

def main():
    print("Number   Is Prime?")
    print("-" * 20)
    for x in range(1, 100+1):
        print(x, "     ", is_prime(x))

if __name__ == "__main__":
    main()