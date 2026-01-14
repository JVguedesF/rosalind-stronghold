# Translating RNA into Protein (PROT)

## Problem Description

Link: [http://rosalind.info/problems/prot/](http://rosalind.info/problems/prot/)

## Solution Logic

Uses a lookup table (dictionary) to map each nucleotide triplet (codon) to its corresponding amino acid.

To read the sequence, it creates an iterator over the RNA string and uses `zip` passing the same iterator three times, which groups nucleotides into tuples of 3 sequentially. The loop is interrupted (`break`) as soon as a "Stop" codon is encountered.
