#!/usr/bin/python
# Valerie Chapple
# Stooge Sort with Python 3
# Oct 2017

import string
import math

# GLOBAL CONSTANTS
FILE_IN_NAME = "data.txt"
FILE_OUT_NAME = "stooge.out"

# FUNCTIONS

# stoogeSort( list, start, end )
# PRE: list is array of integers 
# POST: list is sorted in ascending order
def stoogeSort( list, start, end ):
	n = end - start + 1	# number of elements in range
	# BASE
	if (n == 2):    # Check if needing to swap for lists with only two values
		if (list[start] > list[end]):
			tmp = list[start]
			list[start] = list[end]
			list[end] = tmp
		return
	if (n <= 1):
		return
	# RECURSION
	i = math.ceil(n*2/3) # ceiling of 2/3 the length of the list
	stoogeSort(list, start, i-1 + start)
	stoogeSort(list, end-i+1, end)
	stoogeSort(list, start, i-1 + start)
	return



# MAIN PROGRAM

# Open file called FILE_IN_NAME
dataFile = open( FILE_IN_NAME, "r" );

# Create empty file called FILE_OUT_NAME
resultFile = open( FILE_OUT_NAME, "w" );

# Loop until end of file
for line in dataFile:
	intArray = line.split()
	intArray = [int(i) for i in intArray]

	# Call sort
	stoogeSort( intArray, 0, len(intArray)-1 )

	# Save sorted list to next line of FILE_OUT_NAME
	sortedString = "";
	for i in intArray:
		sortedString += str(i)
		sortedString += " "
	sortedString.strip()
	resultFile.write(sortedString)
	resultFile.write("\n")

# Close files
dataFile.close()
resultFile.close()
