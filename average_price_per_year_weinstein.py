"""This program reads a text file, GasPrices.txt, which has the weekly average gas prices between April 1993 and August 2013. This program takes that information and returns the average price per year.

Programmer: David Weinstein
Date: 10/30/2019
File name: average_price_per_year_weinstein.py

Pseudocode:
1.Set up dictionaries for the yearly price, and the yearly count (so we can get the average).
2. Define manageGasFile function which will split our file into workable lists
    2a. open file
    2b. read the file by line
    2c. split each line into a list which seperates the date into the first element and price into the second element
3. Seperate the date so we can access the year, and convert the price into a floating number
    3a. using the year as the dictionary key, we add the price up by year, and add 1 to the count so we can get the average
4. Get the average price per year by dividing the price value by the count value for each key in the dictionaries
    4a. print the results
"""
#set up dictionaries for yearly price and count
YEARS_PRICE = {'1993':0.0, '1994':0.0, '1995':0.0, '1996':0.0, '1997':0.0, '1998':0.0, '1999':0.0, '2000':0.0, '2001':0.0, '2002':0.0, '2003':0.0, '2004':0.0, '2005':0.0, '2006':0.0, '2007':0.0, '2008':0.0, '2009':0.0, '2010':0.0, '2011':0.0, '2012':0.0, '2013':0.0}
YEARS_COUNT = {'1993':0.0, '1994':0.0, '1995':0.0, '1996':0.0, '1997':0.0, '1998':0.0, '1999':0.0, '2000':0.0, '2001':0.0, '2002':0.0, '2003':0.0, '2004':0.0, '2005':0.0, '2006':0.0, '2007':0.0, '2008':0.0, '2009':0.0, '2010':0.0, '2011':0.0, '2012':0.0, '2013':0.0}

def manageGasFile(f):
    """opens file, splits into list of date, and price. seperates price by year into dictionary. then get average price per year of gas"""
    gasFile = open(f, 'r')
    lines = gasFile.readlines()
    splitLines = []
    # split the lines of text into list, seperating the date and price
    for line in lines:
        splitLines.append(line.split(':'))
    # set the date as first element for each line, split up the date so we can access the year at the last index, set the price as a floating number, access and change the dictionaries values using the year as the key 
    for ele in splitLines:
        date = ele[0]
        splitDate = date.split('-')
        year = splitDate[-1]
        price = float(ele[1])
        YEARS_PRICE[year] += price
        YEARS_COUNT[year] += 1
    # take the average by taking the value from the years_price dictionary, and dividing by the value in the years_count dictionary for each key, print the results
    count = 0
    while count < len(YEARS_PRICE):
        for key in YEARS_PRICE:
            avg = YEARS_PRICE[key] / YEARS_COUNT[key]
            count +=1
            print("The average price in " + key + " was $" + "%.2f" % avg)

def main():
    manageGasFile("../GasPrices.txt")

if __name__ == "__main__":
    main()
