# Counting Point Mutations (HAMM)

**URL:** http://rosalind.info/problems/hamm/

## Solution

Calculates the Hamming distance between two DNA strands. Uses `zip` to iterate simultaneously over the sequences and `sum` with a generator expression to count positions where nucleotides diverge.
