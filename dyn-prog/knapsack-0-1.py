#!/usr/bin/python
# Valerie Chapple
# 0/1 Knapsack  with Python 3
# Nov 2017

import string

maxW = 0
items = []

maxWeights = [
    5,  # Set 0
    165 # Set 1
]

weights = [
[ 2, 3, 4, 5 ], # Set 0
[ 23, 31, 29, 44, 53, 38, 63, 85, 89, 82 ] # Set 1
]

profits = [
[ 3, 4, 5, 6 ], # Set 0
[ 92, 57, 49, 68, 60, 43, 67, 84, 87, 72 ] # Set 1
]
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

def setMax( m ):
    global maxW 
    maxW = m

def setItems( i ):
    global items 
    items = i 

# initItems( )
# PRE: None
# POST: returns list of objects of type Item
def initItems( setNum ):
    items = []
    items.append( None ) 

    #if setNum == 0:
        #items.append( Item( 2, 3 ) )
        #items.append( Item( 3, 4 ) )
        #items.append( Item( 4, 5 ) )
        #items.append( Item( 5, 6 ) ) 
    wArray = weights[ setNum ]
    pArray = profits[ setNum ]

    for i in range( len(wArray) ):
        items.append( Item( wArray[i], pArray[i] ) )
    setItems(items)

def initMax( setNum ):
    setMax( maxWeights[ setNum ] )

def initScene( setNum):
    initMax( setNum )
    initItems( setNum)


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

    setNum = 1
    initScene( setNum )
 
    n = len(items) - 1 # index 1 based

    numRows = n + 1
    numCols = maxW + 1
    benefit = [[ 0 for j in range( numCols ) ] for i in range( numRows ) ]


    for i in range( 1, numRows ):
        for w in range( 1, numCols ):
            if items[i].getW() > w:
                benefit[i][w] = benefit[ i-1][ w ]
            else:
                skipItem = benefit[ i-1 ][ w ]
                addItem = benefit[ i-1 ][ w - items[i].getW() ] + items[i].getB()                
                benefit[i][w] = max( skipItem, addItem ) 

    # Print Array
#    printArray( benefit , numRows , numCols )

    # Print Max benefit
    print( benefit[ n ][ maxW ] )


main()
