#!/usr/bin/python
# Valerie Chapple
# Merge Sort with Python 3
# Oct 2017

import string

# GLOBAL CONSTANTS
FILE_IN_NAME = "data.txt"
FILE_OUT_NAME = "merge.out"


# FUNCTIONS

# mergeSort( list )
# PRE: list must be list of integers
# POST: list is sorted in ascending order
def mergeSort( list ):
	# BASE CASE
	if len(list) <= 1:
		return list
	
	# RECURSION CASE
	# Divide list into two lists
	middle = len(list)//2 # floor division: https://docs.python.org/3/tutorial/introduction.html
	list1 = list[:middle] # Cite: slicing: https://docs.python.org/3/tutorial/introduction.html
	list2 = list[middle:]

	# Call mergeSort recursively on both new lists
	list1 = mergeSort( list1)
	list2 = mergeSort( list2)

	# Merge Two lists together as new list
	mergedList = []
	merge( list1, list2, mergedList )	
	return mergedList

# merge( list1, list2 )
# PRE: list1 and list2 are lists of integers
# POST: list1 and list2 are joined together in ascending order
def merge( list1, list2, mergedList):
	
	i1 = 0;
	i2 = 0;

	# While list1 and list2 are not at the end
	while i1 < len(list1) and i2 < len(list2):
		# Compare current ints of each list for smallest value
		if list1[i1] <= list2[i2]:
			# Move list1[i1] to mergedList and move to next index
			mergedList.append(list1[i1])
			i1 += 1
		else:
			# Move list2[i2] to mergedList and move to next index
			mergedList.append(list2[i2])
			i2 += 1

	# Add remaining list if any to end of mergedList
	while i1 < len(list1):
		# Add list1 to mergedList
		mergedList.append(list1[i1])
		i1 += 1

	while i2 < len(list2):
		# Add list2 to mergedList
		mergedList.append(list2[i2])
		i2 += 1



# MAIN PROGRAM

# Open file called FILE_IN_NAME
dataFile = open( FILE_IN_NAME, "r" );

# Create empty file called FILE_OUT_NAME
resultFile = open( FILE_OUT_NAME, "w" );

# Loop until end of file
for line in dataFile:
	intArray = line.split() 
	intArray = [int(i) for i in intArray]

	# Call mergeSort
	sortedArray = mergeSort( intArray )

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
