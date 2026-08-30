# Sorting Benchmark

Comparing Bubble Sort against Python's built-in Timsort to see how
algorithm choice affects real runtime.

## Results

Tested on randomly generated integers (1 to 1000).

| Input size | Bubble Sort | Python sorted() |
|---|---|---|
| 1,000 | 0.040 s | — |
| 10,000 | 4.404 s | 0.00076 s |

**At n = 10,000, Timsort was about 5,800x faster.**

## Why the gap

Bubble Sort is O(n²). Increasing input 10x (1,000 to 10,000) increased
its runtime about 107x, close to the expected 100x.

Timsort is O(n log n), so it scales far better as input grows.

## Running it
