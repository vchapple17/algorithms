# Insertion Sort

## Description
Insertion sort starts by examining the first two elements in a list.  If the first element is greater than the second element, they are swapped.  Then, the third element is examined with the second element. If the third element is less than the second, they are swapped, and then if the third element (now in the second spot) is less than the first element, the third element (now in the second spot) is swapped with the first element.  Then, the fourth element is examined against the third, and swapped if needed.  Swapping continues until the element being sorted is greater than the item preceeding it.

### Example
Sort:   `[50, 20, 40, 30, 70, 10]`

#### Examine First Two Elements
`[50, 20]` --> Compare 20 and 50: 20 is less than 50, so they swap. Then, look at the next element.<br>
`[20, 50]` -->  End of list, go to next element if there are any.<br>

#### Examine First Three Elements
`[20, 50, 40]` -->  Compare 40 and 50: 40 is less than 50, so they swap<br>
`[20, 40, 50]` -->  Compare 40 and 20: 40 is greater than 20, look at the next element if there is one.<br>

#### Examine First Four Elements
`[20, 40, 50, 30]` -->  Compare 30 and 50: 30 is less than 50, so they swap<br>
`[20, 40, 30, 50]` -->  Compare 30 and 40: 30 is less than 40, so they swap<br>
`[20, 30, 40, 50]` -->  Compare 30 and 50: 30 is greater than 20, look at the next element if there is one.<br>

#### Examine First Five Elements
`[20, 30, 40, 50, 70]` -->  Compare 70 and 50: 70 is greater than 50, look at the next element if there is one.<br>

#### Examine First Six Elements
`[20, 30, 40, 50, 70, 10]` -->  Compare 10 and 70: 10 is less than 70, so they swap<br>
`[20, 30, 40, 50, 10, 70]` -->  Compare 10 and 50: 10 is less than 50, so they swap<br>
`[20, 30, 40, 10, 50, 70]` -->  Compare 10 and 40: 10 is less than 40, so they swap<br>
`[20, 30, 10, 40, 50, 70]` -->  Compare 10 and 30: 10 is less than 30, so they swap<br>
`[20, 10, 30, 40, 50, 70]` -->  Compare 10 and 20: 10 is less than 20, so they swap<br>
`[10, 20, 30, 40, 50, 70]` -->  End of list, go to next element if there are any.<br>

#### List is sorted.
`[10, 20, 30, 40, 50, 70]`

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
The experimental running time for Insertion sort is directly related to the square of the size of the input, which aligns with the theoretical running time of Θ(n<sup>2</sup>) on average.
