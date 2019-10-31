"""This program reads a text file, GasPrices.txt, which has the weekly average gas prices between April 1993 and August 2013. This program takes that information and returns the average price per year.

Programmer: David Weinstein
Date: 10/30/2019
File name: average_price_per_year_weinstein.py

Pseudocode:
1.
"""

YEARS_PRICE = {'1993':0.0, '1994':0.0, '1995':0.0, '1996':0.0, '1997':0.0, '1998':0.0, '1999':0.0, '2000':0.0, '2001':0.0, '2002':0.0, '2003':0.0, '2004':0.0, '2005':0.0, '2006':0.0, '2007':0.0, '2008':0.0, '2009':0.0, '2010':0.0, '2011':0.0, '2012':0.0, '2013':0.0}
YEARS_COUNT = {'1993':0.0, '1994':0.0, '1995':0.0, '1996':0.0, '1997':0.0, '1998':0.0, '1999':0.0, '2000':0.0, '2001':0.0, '2002':0.0, '2003':0.0, '2004':0.0, '2005':0.0, '2006':0.0, '2007':0.0, '2008':0.0, '2009':0.0, '2010':0.0, '2011':0.0, '2012':0.0, '2013':0.0}

gasFile = open("../GasPrices.txt", 'r')
lines = gasFile.readlines()
splitLines = []
for line in lines:
    splitLines.append(line.split(':'))

for ele in splitLines:
    date = ele[0]
    splitDate = date.split('-')
    year = splitDate[-1]
    price = float(ele[1])
    YEARS_PRICE[year] += price
    YEARS_COUNT[year] += 1

count = 0
while count < len(YEARS_PRICE):
    for key in YEARS_PRICE:
        avg = YEARS_PRICE[key] / YEARS_COUNT[key]
        count +=1
        print("The average price in " + key + " was $" + "%.2f" % avg)
