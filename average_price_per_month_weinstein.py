"""This program uses the text file GasPrices.txt, which has the weekly average gas prices from April 1993 to August 2013. This program uses that data and returns the average price of gas per month.

Programmer: David Weinstein
Date: 11/1/2019
File name: average_price_per_month_weinstein.py

Pseudocode:
"""
MONTHS = ['04', '05', '06', '07', '08', '09', '10', '11', '12', '01', '02', '03']
MONTHS_TO_TEXT = {'01':'January', '02':'February', '03':'March', '04':'April', '05':'May', '06':'June', '07':'July', '08':'August', '09':'September', '10':'October', '11':'November', '12':'December'}
YEARS = ['1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013']

def manageGasFile(f):
    gasFile = open(f, 'r')
    lines = gasFile.readlines()
    splitLines(lines)

def splitLines(lyst):
    newList = []
    mainList = []
    for line in lyst:
        newList.append(line.split(':'))
    for ele in newList:
        date = ele[0]
        splitDate = date.split('-')
        month = splitDate[0]
        year = splitDate[-1]
        price = float(ele[1])
        mainList.append([month, year, price])
    countAvg(mainList)

def countAvg(lyst):
    total = 0.0
    count = 0
    avgList = []
    for ele in lyst:
        if ele[0] == MONTHS[0] and ele[1] == YEARS[0]:
            avgList.append(ele[2])
            avg = sum(avgList) / len(avgList)
    print(avg)


            

def main():
    manageGasFile("../GasPrices.txt")

if __name__ == "__main__":
    main()