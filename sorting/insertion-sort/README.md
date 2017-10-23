# Insertion Sort

## Description

## Theoretical Running Time


## insertsort.py

### Usage
`python3 insertsort.py`

### Input
Input is from a file called `data.txt`.  Each line in `data.txt` is an input to sort.  That is, a list of integers separated by spaces.

### Output
The sorted inputs (each line) are written to a file called `insert.out` in the same line-order that is in the `data.txt` input.

## Experimental Running Time

# Data & Graph
Array size is denoted by the variable `n`.

| n | Time (s) |
| ---------- | -------- |
| 500  |  0.07|
| 1000  |  0.38|
| 2000  |  1.09|
| 4000  |  3.85|
| 5000  |  8.11|
| 10000  |  24.84|
| 20000  |  92.65|
| 30000  |  246.11|
| 50000  |  675.21|

Running Time vs. n<br>
<img alt="Insertion Running Time" src="https://github.com/vchapple17/algorithms/blob/master/sorting/insertion-sort/img/insert-linear.png" height="350">

Running Time vs. n<sup>2</sup><br>
<img alt="Insertion Running Time" src="https://github.com/vchapple17/algorithms/blob/master/sorting/insertion-sort/img/insert-n-squared.png" height="350">

# Conclusion
The experimental running time for Insertion sort is directly related to the square of the size of the input, which aligns with the theoretical running time of Θ(n<sup>2</sup>).
