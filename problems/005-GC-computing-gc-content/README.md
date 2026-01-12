# Computing GC Content (GC)

**URL:** http://rosalind.info/problems/gc/

## Solution

Reads the FASTA file using a `read_fasta` helper function implemented with line-by-line reading (streaming) for memory efficiency. Iterates over the resulting dictionary calculating the percentage of 'G' and 'C' bases and identifies the record with the highest GC content via direct comparison.
