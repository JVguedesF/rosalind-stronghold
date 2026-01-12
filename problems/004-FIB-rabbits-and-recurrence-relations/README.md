# Rabbits and Recurrence Relations (FIB)

**URL:** http://rosalind.info/problems/fib/

## Solution

Calculates the total number of rabbit pairs after $n$ months using a variation of the Fibonacci sequence. Applies the recurrence relation $F_n = F_{n-1} + (k \times F_{n-2})$, where $k$ represents the litter size, considering that only rabbits older than one month (generation $n-2$) are able to reproduce.
