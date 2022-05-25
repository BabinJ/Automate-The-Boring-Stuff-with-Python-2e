# Table Printer

# tablePrinter.py - Write a function named printTable() that takes a list of lists of strings and displays it in a well-organized
# table with each column right-justified. Assume that all the inner lists will contain the same number of strings

# Define the printTable() function to do the things


tableData = [['apples','oranges','cherries','banana'],
             ['Alice','Bob','Carol','David'],
             ['dogs','cats','moose','goose']]

def printTable(table):
    # Create am empty list of columnwidths
    colWidths = [0] * len(table)

    # Populate the columnwidths by looping through tableData
    for col in range(len(colWidths)):
        maxLen = 0
        for i in table[col]:
            if len(i) > maxLen:
                maxLen = len(i)
        colWidths[col] = maxLen

    # Print out the table
    for i in range(len(table[0])):
        for j in range(len(table)):
            print(table[j][i].rjust(colWidths[j]), " ", end=" ")
        print()

printTable(tableData)