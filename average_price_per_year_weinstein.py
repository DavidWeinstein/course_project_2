"""This program uses a text file, GasPrices.txt, which has the weekly average gas prices between April 1993 and August 2013. This program takes that information and returns the average price per year.

Programmer: David Weinstein
Date: 10/30/2019
File name: average_price_per_year_weinstein.py

Pseudocode:
1.
"""

def organize(f):
    openFile = open(f, 'r')
    lines = openFile.readlines()
    lyst = []
    for line in lines:
        splitLines = line.split(':')
        dates = splitLines[0].split('-')
        prices = float(splitLines[1])
        if dates[2] == '2013':
            lyst.append(prices)
    return lyst

# def average(list):

def main():
    print(organize("../GasPrices.txt"))

if __name__ == "__main__":
    main()