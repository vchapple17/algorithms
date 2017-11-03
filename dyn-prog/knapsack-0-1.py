#!/usr/bin/python
# Valerie Chapple
# 0/1 Knapsack  with Python 3
# Nov 2017

import string

# GLOBAL CONSTANTS
MAX_W = 20

# CLASSES
class Item:
    def __init__(self, weight, benefit):
        self.w = weight
        self.b = benefit
    def getB(self):
        return self.b
    def getW(self):
        return self.w

# FUNCTIONS
# initItems( )
# PRE: None
# POST: returns list of objects of type Item
def initItems( ):
    items = []
    items.append( Item( 2, 3 ) )
    items.append( Item( 3, 4 ) )
    items.append( Item( 4, 5 ) )
    items.append( Item( 5, 6 ) ) 
    return items

def printArray( array, r, c ):
    # Heading
    heading = "i \ w\t"
    line = "------\t"
    for col in range( c ):
        heading += str(col) + "\t"
        line += "--\t"

    print(heading)
    print(line)


    for i in range( r ):
        row = str(i) + "\t" 
        for j in range( c ):
            row += str(array[i][j]) + "\t"
        print(row)

    
# main()
# PRE: None
# POST: Print max benefit of having Items and MAX_W
def main():
    items = initItems()
    n = len(items)

    numCols = 5
    numRows = 10 
    array = [[ 0 for j in range( numCols + 1) ] for i in range( numRows ) ]
    printArray( array, numRows, numCols + 1 )



main()
