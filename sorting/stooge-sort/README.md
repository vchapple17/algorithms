# Stooge Sort

## Description
Stooge sort is an inefficient sorting algorithm.  StoogeSort sorts the first 2/3 of a list of items recursively to the base case of having a list of two items. If the two items are out of order, they are swapped, and the recursion unwinds.  StoogeSort, then, recursively sorts the last 2/3 of the list, again to the base case. Lastly, the StoogeSort recursively sorts the first 2/3 of the list a second time, as the last portion of it may now be unsorted.

## Theoretical Running Time
Stooge sort has a recursion of T(n) = 3T( 2n/3 ) + Θ(1). Using the master method, T(n) = Θ( n<sup>log<sub>1.5</sub>3</sup>) ~ Θ( n<sup>2.71</sup>)

## stoogesort.py

### Usage
`python3 stoogesort.py`

### Input
Input is from a file called `data.txt`.  Each line in `data.txt` is an input to sort.  That is, a list of integers separated by spaces.

### Output
The sorted inputs (each line) are written to a file called `stooge.out` in the same line-order that is in the `data.txt` input.

## Experimental Running Time

# Data & Graph
Array size is denoted by the variable `n`.

| n | Time (s) |
| ---------- | -------- |
| 50  |  0.020|
| 100  |  0.165|
| 200  |  0.490|
| 400  |  4.465|
| 800  |  41.350|
| 1000  |  41.725|
| 1100  |  125.270|
| 1200  |  125.780|
| 1600  |  375.960|

Running Time vs. n<br>
<img alt="Stooge Running Time" src="https://github.com/vchapple17/algorithms/blob/master/sorting/stooge-sort/img/stooge-power.png" height="350">

# Conclusion
The experimental running time for Stooge sort is directly related to the size of the input to the power of of approximately 2.78, which aligns with the theoretical running time of Θ( n<sup>log<sub>1.5</sub>3</sup>) ~ Θ( n<sup>2.71</sup>).
