# Merge Sort

## Description
Merge sort is a divide and conquer algorithm. It recursively takes a large problem and divides it into two relatively equal subproblems until the size of a subproblem is one element. A subproblem of size one is sorted.  To combine the sorted subproblems of one back together, a merge function is used.

## Theoretical Running Time
Merge sort divides a problem into two subproblems that are approximately half of the total problem. The recursion is approximately *T(n) = 2 T( n/2 ) + n*, as technically the two halves of an odd-sized problem will required the floor and ceiling of *n/2*.  The running time for a merge sort algorithm is *Θ(n lg n)*.

## mergesort.py

### Usage
`python3 mergesort.py`

### Input
Input is from a file called `data.txt`.  Each line in `data.txt` is an input to sort.  That is, a list of integers separated by spaces.

### Output
The sorted inputs (each line) are written to a file called `merge.out` in the same line-order that is in the `data.txt` input.

## Experimental Running Time

# Data & Graph
Array size is denoted by the variable `n`.
| n | Time (s) |
| ---------- | -------- |
| 500	| 0.002 |
| 1000 | 0.006 |
| 2000 | 0.013 |
| 4000 | 0.029 |
| 5000 | 0.049 |
| 10000 | 0.088 |
| 20000 | 0.171 |
| 30000 | 0.297 |
| 50000 | 0.512 |
| 100000 | 0.947 |
| 200000 | 1.826 |
| 300000 | 3.185 |

Running Time vs. n<br>
<img alt="Merge Running Time" src="https://github.com/vchapple17/algorithms/blob/master/sorting/merge-sort/img/mergesort-linear.png" height="350">

Running Time vs. n lg n<br>
<img alt="Merge Running Time" src="https://github.com/vchapple17/algorithms/blob/master/sorting/merge-sort/img/mergesort-nlgn.png" height="350">

# Conclusion
The experimental running time for merge sort is directly related to the size of the input. A slightly better fit is the running time vs. n lg n, which aligns with the theoretical running time of Θ(n lg n).
