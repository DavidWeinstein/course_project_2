"""This program will output all numbers in a given range (default is 1 to 100) and tell us if the number is prime or not.

Programmer: David Weinstein
Date: 10/30/2019
File name: prime_numbers_weinstein.py

Pseudocode:
1. Make helper function of is_prime(num), which checks if a number is prime or not
    1a. Check if number is divisible with any number from range 2 up to, but not including the number
    1b. If the number is not divisilbe by any number in that range, then it must be prime
2. Define main function which sets up our text output chart
    2a. Check numbers from range 1 to 100 + 1
    2b. Print the number we are checking, and then print the output for the helper function is_prime(number)
"""
# helper function returns not prime if number is divisilbe by anything between 2 and the current num, and returns prime otherwise
def is_prime(num):
    for x in range(2, num):
        if num % x == 0:
            return "Not Prime"
    return "Prime"

#main function sets up list and calls the is_prime helper function
def main():
    print("Number   Is Prime?")
    print("-" * 20)
    for x in range(1, 100+1):
        print("%-8d" % x, is_prime(x))

if __name__ == "__main__":
    main()
    