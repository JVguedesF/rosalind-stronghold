# Complementing a Strand of DNA (REVC)

**URL:** http://rosalind.info/problems/revc/

## Solution

Generates the reverse complement of the DNA strand. Utilizes `str.maketrans` and `translate` to perform the simultaneous substitution of base pairs (A ↔ T, C ↔ G) and `[::-1]` to reverse the resulting sequence.
