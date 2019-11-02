"""This program uses the text file GasPrices.txt, which has the weekly average gas prices from April 1993 to August 2013. This program uses that data and returns the average price of gas per month.

Programmer: David Weinstein
Date: 11/1/2019
File name: average_price_per_month_weinstein.py

Pseudocode:
"""
MONTHS = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
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
    count = 0
    mnthIdx = 3
    yrIdx = 0
    sumList = []
    avgList = []
    while count < len(lyst):
        month = lyst[count][0]
        year = lyst[count][1]
        price = float(lyst[count][2])
        if month == MONTHS[mnthIdx] and year == YEARS[yrIdx]:
            sumList.append(price)
            avg = float(sum(sumList) / len(sumList))
            avgList.append(avg)
        else:
            print("Average price for "+ MONTHS_TO_TEXT[MONTHS[mnthIdx]]+", "+ YEARS[yrIdx] + ": $" + "%.2f" % avg)
            mnthIdx += 1
            sumList = []
            if mnthIdx == len(MONTHS):
                yrIdx += 1
                mnthIdx = 0
            if yrIdx == len(YEARS):
                break
        count += 1

def main():
    manageGasFile("../GasPrices.txt")

if __name__ == "__main__":
    main()
