#! /usr/bin/python3
# Practice: Table Printer

def printTable(list, colWidths):

    debug = 0 # debugging mode

    # find the longest string in each of the inner lists
    listSize = len(list)
    colWidths = [0] * listSize
    for i in range(0, listSize):
        innerSize = len(list[i])
        longest = 0
        for j in range (0, innerSize):
            if len(list[i][j]) > longest:
                longest = len(list[i][j])
                word = list[i][j]

        if debug == 1:
            print('The longest string in the inner list ' + str(i) + ' is: ' + word + ' with ' + str(longest) + ' letters.')

        # store the maximum width of each column as a list of integers
        colWidths[i] = longest

        if debug == 1:
            print(colWidths)

    # "rotate" and print the list of lists
    y = 0
    for x in range(0, len(list[y])):
        for y in range(len(list)):
            print(list[y][x].rjust(colWidths[y]), end = ' ')
        print()




tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData, 20)
