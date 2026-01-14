# Finding a Motif in DNA (SUBS)

## Problem Description

Link: [http://rosalind.info/problems/subs/](http://rosalind.info/problems/subs/)

## Solution Logic

Takes two DNA strings: the main sequence and the motif.

The solution iterates through all indices of the main sequence using a list comprehension. For each index `i`, it checks if the slice starting at that position matches the motif using the `startswith` method. Returns the positions where matches are found, adjusted to 1-based indexing.
