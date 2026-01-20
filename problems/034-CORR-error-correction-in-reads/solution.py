from utils.io import read_fasta
from collections import Counter

def reverse_complement(seq):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return "".join(complement[base] for base in seq[::-1])

def hamming_distance(s1, s2):
    return sum(1 for a, b in zip(s1, s2) if a != b)

def solve():
    data = read_fasta()
    reads = list(data.values())

    counts = Counter(reads)
    
    correct_reads = set()
    incorrect_reads = []

    for r in reads:
        rev = reverse_complement(r)
        if counts[r] + counts.get(rev, 0) >= 2:
            correct_reads.add(r)
        else:
            incorrect_reads.append(r)
            
    correction_pool = correct_reads.union({reverse_complement(r) for r in correct_reads})

    results = []

    for inc in incorrect_reads:
        for corr in correction_pool:
            if hamming_distance(inc, corr) == 1:
                results.append(f"{inc}->{corr}")
                break
                
    return "\n".join(results)

if __name__ == "__main__":
    print(solve())