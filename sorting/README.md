# Merge Sort
## Description
Merge sort is a divide and conquer algorithm. It recursively takes a large problem and divides it into two relatively equal subproblems until the size of a subproblem is one element. A subproblem of size one is sorted.  To combine the sorted subproblems of one back together, a merge function is used.
## Analysis
Merge sort divides a problem into two subproblems that are approximately half of the total problem. The recursion is approximately *T(n) = 2 T( n/2 ) + n*, as technically the two halves of an odd-sized problem will required the floor and ceiling of *n/2*.  The running time for a merge sort algorithm is *Θ(n lg n)*.
## mergesort.py
### Usage
`python3 mergesort.py`
### Input
Input is from a file called `data.txt`.  Each line in `data.txt` is an input to sort.  That is, a list of integers separated by spaces.
### Output
The sorted inputs are written to a file called `merge.out` in the same order that is in the `data.txt` input.

