#!/usr/bin/python
# Valerie Chapple
# Insertion sort with Python 3
# Oct 2017

import string

# GLOBAL CONSTANTS
FILE_IN_NAME = "data.txt"
FILE_OUT_NAME = "insert.out"

# FUNCTIONS

# insertionSort( list )
# Sorts array in place least to greatest
# PRE: list must be list of integers
# POST: list is sorted in ascending order
def insertionSort( list ):
	indexToSort = 1
	while indexToSort < len(list):
		key = indexToSort 
		# Compare current number (key) to previous on list
		while key > 0 and list[key - 1] >  list[key]:
			# Value at key is less than previous, so swap
			tmp = list[key - 1]
			list[key - 1] = list[key]
			list[key] = tmp
			#Update the index of key, as it just moved
			key = key - 1
		# Update indexToSort to next index value
		indexToSort += 1
	return list	





# MAIN PROGRAM

# Open file called FILE_IN_NAME
dataFile = open( FILE_IN_NAME, "r" );

# Create empty file called FILE_OUT_NAME
resultFile = open( FILE_OUT_NAME, "w" );

# Loop until end of file
for line in dataFile:
	intArray = line.split() 
	intArray = [int(i) for i in intArray]
	
	# Call insertionSort
	sortedArray = insertionSort( intArray )

	# Save sorted list to next line of FILE_OUT_NAME
	sortedString = "";
	for i in sortedArray:
		sortedString += str(i)
		sortedString += " "
	sortedString.strip()
	resultFile.write(sortedString)
	resultFile.write("\n")

# Close files
dataFile.close()
resultFile.close()
