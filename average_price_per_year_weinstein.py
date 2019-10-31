"""This program reads a text file, GasPrices.txt, which has the weekly average gas prices between April 1993 and August 2013. This program takes that information and returns the average price per year.

Programmer: David Weinstein
Date: 10/30/2019
File name: average_price_per_year_weinstein.py

Pseudocode:
1.
"""
import math

YEARS = ['1993','1994','1995','1996']

gasFile = open("../GasPrices.txt", 'r')
lines = gasFile.readlines()
splitLines = []
for line in lines:
    splitLines.append(line.split(':'))
yearlyPrices = []
date = ''
price = ''
for ele in splitLines:
    date = ele[0]
    price = float(ele[1])
count = 0
while count < len(YEARS):
    if YEARS[count] in date:
        yearlyPrices.append(price)
        avg = "%.2f" % (sum(yearlyPrices) / len(yearlyPrices))
        print(avg)
    count += 1
    
# print(len(YEARS))
# print(YEARS)
# print(ninetyThree)
# print("%.2f" % (sum(ninetyThree) / len(ninetyThree)))
# print(splitLines)