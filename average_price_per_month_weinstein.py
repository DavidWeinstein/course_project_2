"""This program uses the text file GasPrices.txt, which has the weekly average gas prices from April 1993 to August 2013. This program uses that data and returns the average price of gas per month.

Programmer: David Weinstein
Date: 11/1/2019
File name: average_price_per_month_weinstein.py

Pseudocode:
1. Set up constants for months, years and months to text dictionary
2. Open the file and put into list of lines
3.Split lines into list of date and price
    3a.Split date into month, day, year to access month and year
    3b.Populate list of month, year, price to calculate average price per month
4.Loop through list checking each sublist
    4a.If price is in month and year, populate list to average
    4b.Else print the desired output for month, set count to count - 1 to not skip any list, reset the average list, and index the month
        4b.1Check if we are atthe last month, if we are reset month index and index through to the next year
    4c.Print last output for last month in text file
"""
# Constants for months, years, and months to text dictionary.
MONTHS = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
MONTHS_TO_TEXT = {'01':'January', '02':'February', '03':'March', '04':'April', '05':'May', '06':'June', '07':'July', '08':'August', '09':'September', '10':'October', '11':'November', '12':'December'}
YEARS = ['1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013']

def openGasFile(f):
    """Opens gas file, puts lines of text into list"""
    gasFile = open(f, 'r')
    lines = gasFile.readlines()
    splitLines(lines)

def splitLines(lyst):
    """Splits lines of text into [date, price] format, and then splits that list into [month, year, price] format"""
    #Set up empty list for date and price, and for the main working list to solve average
    datePriceList = []
    mainList = []
    for line in lyst:
        #Populate list with date and price
        datePriceList.append(line.split(':'))
    for ele in datePriceList:
        date = ele[0]
        #Split date into month, day, year to access month and year
        splitDate = date.split('-')
        month = splitDate[0]
        year = splitDate[-1]
        #Set price as floating number value of the second element of datePriceList
        price = float(ele[1])
        #Populate main workable list of lists in month, year, price format
        mainList.append([month, year, price])
    countAvg(mainList)

def countAvg(lyst):
    """Calculates and outputs average price per gallon for each month from April, 1993 to August 2013"""
    #Set up counter for while loop, month index to iterate through months strarting at index 3, year index to iterate through all the years, and empty list for calculating the average
    count = 0
    mnthIdx = 3
    yrIdx = 0
    avgList = []
    #While loop through entire list
    while count < len(lyst):
        #Set up month, year and price as variables to check every sublist in list.
        month = lyst[count][0]
        year = lyst[count][1]
        price = float(lyst[count][2])
        #If price is in the same month and year, populate list with price to calculate average
        if month == MONTHS[mnthIdx] and year == YEARS[yrIdx]:
            avgList.append(price)
            avg = sum(avgList) / len(avgList)
        else:
            #Else make count equal to current count - 1, so we don't skip over the first week in each month, print desired outout, reset average list to an empty list, and iterate the month index to check next month
            count = count - 1
            print("Average price for "+ MONTHS_TO_TEXT[MONTHS[mnthIdx]]+", "+ YEARS[yrIdx] + ": $" + "%.2f" % avg)
            avgList = []
            mnthIdx += 1
            #Check if month index equal to the length of months list, if it is iterate to the next year and reset month index to 0
            if mnthIdx == len(MONTHS):
                yrIdx += 1
                mnthIdx = 0
        #Iterate count by one to index items in list and control while loop
        count += 1
    #Print last month as it does not make the while loop
    print("Average price for "+ MONTHS_TO_TEXT[MONTHS[mnthIdx]]+", "+ YEARS[yrIdx] + ": $" + "%.2f" % avg)

def main():
    """Open gas file"""
    openGasFile("../GasPrices.txt")

if __name__ == "__main__":
    main()
