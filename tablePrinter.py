#! python3
# tablePrinter.py - Takes a list of lists of strings and
# displays it in a table.

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(data):
    columnWidth = [0] * len(tableData)
    for i in range(3):
        columnWidth[i] = len(max(tableData[i]))
    for i in range(4):
        for y in range(3):
            output = tableData[y][i].rjust(columnWidth[y] + 1)
            print(output, end = ' ')
        print('\n')

printTable(tableData)
